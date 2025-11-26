from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.trainers.models import Trainer
from apps.pokemons.models import Pokemon
from .models import TrainerPokemon
from .serializers import TrainerPokemonSerializer


class AddPokemonToTrainerView(APIView):
    def post(self, request):
        trainer_id = request.data.get("trainer_id")
        pokemon_id = request.data.get("pokemon_id")

        # validar trainer
        try:
            trainer = Trainer.objects.get(id=trainer_id)
        except Trainer.DoesNotExist:
            return Response({"erro": "Treinador não encontrado."}, status=404)

        # validar pokemon
        try:
            pokemon = Pokemon.objects.get(id=pokemon_id)
        except Pokemon.DoesNotExist:
            return Response({"erro": "Pokémon não encontrado."}, status=404)

        # evitar duplicação
        if TrainerPokemon.objects.filter(trainer=trainer, pokemon=pokemon).exists():
            return Response({"erro": "Este Pokémon já está associado."}, status=400)

        relation = TrainerPokemon.objects.create(trainer=trainer, pokemon=pokemon)
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
        return Response({"mensagem": "Pokémon removido."}, status=200)
