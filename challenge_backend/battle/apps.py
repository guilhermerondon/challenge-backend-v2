from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pokemons.models import Pokemon
from relations.models import TrainerPokemon

class PokemonBattleView(APIView):
    def get(self, request, pokemon1_id, pokemon2_id):
        try:
            p1 = Pokemon.objects.get(id=pokemon1_id)
            p2 = Pokemon.objects.get(id=pokemon2_id)
        except Pokemon.DoesNotExist:
            return Response({"error": "Pokémon não encontrado."},
                            status=status.HTTP_404_NOT_FOUND)

        t1 = TrainerPokemon.objects.filter(pokemon=p1).values_list("trainer_id", flat=True)
        t2 = TrainerPokemon.objects.filter(pokemon=p2).values_list("trainer_id", flat=True)

        if set(t1).intersection(set(t2)):
            return Response({"erro": "Pokémons do mesmo treinador."},
                            status=status.HTTP_400_BAD_REQUEST)

        if p1.weight > p2.weight:
            return Response({"vencedor": p1.name})
        elif p2.weight > p1.weight:
            return Response({"vencedor": p2.name})
        return Response({"resultado": "empate"})
