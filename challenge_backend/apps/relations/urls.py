from django.urls import path
from .views import AddPokemonToTrainerView, RemovePokemonFromTrainerView

urlpatterns = [
    path('add/', AddPokemonToTrainerView.as_view(), name="add_pokemon"),
    path('remove/', RemovePokemonFromTrainerView.as_view(), name="remove_pokemon"),
]
