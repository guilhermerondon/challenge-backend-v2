from django.urls import path
from .views import PokemonListCreateView, PokemonDetailView

urlpatterns = [
    path('', PokemonListCreateView.as_view()),
    path('<int:pk>/', PokemonDetailView.as_view()),
]