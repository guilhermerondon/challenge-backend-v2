from rest_framework import serializers  
from .models import Trainer, Pokemon, TrainerPokemon

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'age', 'created_at', 'update_at']

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'photo', 'height', 'weight', 'created_at', 'update_at'] 

class TrainerPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerPokemon
        fields = ['id', 'trainer', 'pokemon']

        