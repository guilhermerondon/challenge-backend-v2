from django.urls import path
from .views import PokemonBattleView

urlpatterns = [
    path('<int:pokemon1_id>/<int:pokemon2_id>/', PokemonBattleView.as_view()),
]