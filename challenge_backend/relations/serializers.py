from rest_framework import serializers
from .models import TrainerPokemon

class TrainerPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerPokemon
        fields = '__all__'
