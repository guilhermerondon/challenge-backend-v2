from django.urls import path
from .views import TrainerPokemonCreateView, TrainerPokemonDeleteView

urlpatterns = [
    path('', TrainerPokemonCreateView.as_view()),
    path('<int:pk>/', TrainerPokemonDeleteView.as_view()),
]
