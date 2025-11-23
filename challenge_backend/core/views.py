from rest_framework import generics
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


