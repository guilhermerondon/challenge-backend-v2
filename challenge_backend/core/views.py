from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import Trainer, Pokemon, TrainerPokemon
from .serializers import TrainerSerializer, PokemonSerializer, TrainerPokemonSerializer   

class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer    


class TrainerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer



class PokemonListCreateView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TrainerPokemonCreateView(generics.CreateAPIView): 
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer


class TrainerPokemonDeleteView(generics.RetrieveDestroyAPIView):    
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer


class PokeAPIView(APIView):
    def get(self, request, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"

        response = requests.get(url)

        if response.status_code != 200:
            return Response(
                {"error": "Pokémon não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        data = response.json()

        pokemon_data = {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "photo": data["sprites"]["front_default"],
        }

        return Response(pokemon_data, status=status.HTTP_200_OK)
    

class PokemonBattleView(APIView):
    def get(self, request, pokemon1_id, pokemon2_id):
        try:
            p1 = Pokemon.objects.get(id=pokemon1_id)
            p2 = Pokemon.objects.get(id=pokemon2_id)
        except Pokemon.DoesNotExist:
            return Response(
                {"error": "Um ou ambos os Pokémons não foram encontrados."},
                status=status.HTTP_404_NOT_FOUND
            )


        trainers_p1 = TrainerPokemon.objects.filter(pokemon=p1).values_list("trainer_id", flat=True)
        trainers_p2 = TrainerPokemon.objects.filter(pokemon=p2).values_list("trainer_id", flat=True)


        if set(trainers_p1).intersection(set(trainers_p2)):
            return Response(
                {"error": "Os Pokémons pertencem ao mesmo treinador."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if p1.weight > p2.weight:
            return Response(
                {"Vencedor": p1.name, "Derrotado": p2.name},
                status=status.HTTP_200_OK
            )
        elif p2.weight > p1.weight:
            return Response(
                {"Vencedor": p2.name, "Derrotado": p1.name},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"resultado": "Empate, Ambos os Pokémons têm o mesmo peso."},
                status=status.HTTP_200_OK
            )