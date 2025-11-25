from rest_framework import serializers
from .models import Pokemon
import requests

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data["name"].lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
        response = requests.get(url)

        if response.status_code != 200:
            raise serializers.ValidationError("Pokémon não encontrado.")

        data = response.json()

        validated_data["photo"] = data["sprites"]["front_default"]
        validated_data["height"] = data["height"]
        validated_data["weight"] = data["weight"]

        return super().create(validated_data)
