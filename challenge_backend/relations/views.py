from rest_framework import generics
from .models import TrainerPokemon
from .serializers import TrainerPokemonSerializer

class TrainerPokemonCreateView(generics.CreateAPIView):
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer

class TrainerPokemonDeleteView(generics.DestroyAPIView):
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer
