from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonListCreateView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
