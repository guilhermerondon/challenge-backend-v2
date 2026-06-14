from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from apps.trainers.models import Trainer
from apps.pokemons.models import Pokemon
from .models import TrainerPokemon
from .serializers import TrainerPokemonSerializer

class TrainerPokemonListView(APIView):
    @method_decorator(cache_page(600, key_prefix="relations_list"))
    def get(self, request):
        relations = TrainerPokemon.objects.all()
        serializer = TrainerPokemonSerializer(relations, many=True)
        return Response(serializer.data)

class AddPokemonToTrainerView(APIView):
    def post(self, request):
        trainer_id = request.data.get("trainer_id")
        pokemon_id = request.data.get("pokemon_id")

        try:
            trainer = Trainer.objects.get(id=trainer_id)
        except Trainer.DoesNotExist:
            return Response({"erro": "Treinador não encontrado."}, status=404)

        try:
            pokemon = Pokemon.objects.get(id=pokemon_id)
        except Pokemon.DoesNotExist:
            return Response({"erro": "Pokémon não encontrado."}, status=404)

        if TrainerPokemon.objects.filter(trainer=trainer, pokemon=pokemon).exists():
            return Response({"erro": "Este Pokémon já está associado."}, status=400)

        relation = TrainerPokemon.objects.create(trainer=trainer, pokemon=pokemon)
        
        # Invalidate cache
        cache.clear()

        serializer = TrainerPokemonSerializer(relation)
        return Response(serializer.data, status=201)

class RemovePokemonFromTrainerView(APIView):
    def delete(self, request):
        trainer_id = request.data.get("trainer_id")
        pokemon_id = request.data.get("pokemon_id")

        try:
            relation = TrainerPokemon.objects.get(
                trainer_id=trainer_id,
                pokemon_id=pokemon_id
            )
        except TrainerPokemon.DoesNotExist:
            return Response(
                {"erro": "Este Pokémon não está associado a este treinador."},
                status=404
            )

        relation.delete()
        
        # Invalidate cache
        cache.clear()
        
        return Response({"mensagem": "Pokémon removido."}, status=200)
