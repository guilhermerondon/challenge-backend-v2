from django.urls import path
from .views import (
  TrainerListCreateView, PokemonListCreateView, TrainerPokemonCreateView, TrainerDetailView, PokemonDetailView, TrainerPokemonDeleteView
)

urlpatterns = [
    path('trainers/', TrainerListCreateView.as_view()),
    path('trainers/<int:pk>/', TrainerDetailView.as_view()),

    path('pokemons/', PokemonListCreateView.as_view()),
    path('pokemons/<int:pk>/', PokemonDetailView.as_view()),    

    path('trainer-pokemons/', TrainerPokemonCreateView.as_view()),
    path('trainer-pokemons/<int:pk>/', TrainerPokemonDeleteView.as_view()),
]  