from django.urls import path
from .views import AddPokemonToTrainerView, RemovePokemonFromTrainerView, TrainerPokemonListView

urlpatterns = [
    path('', TrainerPokemonListView.as_view(), name="list_relations"),
    path('add/', AddPokemonToTrainerView.as_view(), name="add_pokemon"),
    path('remove/', RemovePokemonFromTrainerView.as_view(), name="remove_pokemon"),
]
