from rest_framework import serializers
from django.core.cache import cache
import requests
from .models import Pokemon

def fetch_pokemon_data(name):
    cache_key = f"pokeapi_{name.lower()}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}/"
    response = requests.get(url)

    if response.status_code != 200:
        raise serializers.ValidationError({"erro": "Pokémon não encontrado na PokeAPI."})

    data = response.json()
    result = {
        "image": data["sprites"]["front_default"],
        "height": data["height"],
        "weight": data["weight"],
    }
    
    # Save to cache for 10 minutes (600 seconds)
    cache.set(cache_key, result, 600)
    return result

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'image', 'height', 'weight', 'created_at', 'updated_at']
        read_only_fields = ['image', 'height', 'weight', 'created_at', 'updated_at']

    def create(self, validated_data):
        name = validated_data.get("name")
        poke_data = fetch_pokemon_data(name)
        
        validated_data["image"] = poke_data["image"]
        validated_data["height"] = poke_data["height"]
        validated_data["weight"] = poke_data["weight"]

        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get("name")
        if name and name.lower() != instance.name.lower():
            poke_data = fetch_pokemon_data(name)
            validated_data["image"] = poke_data["image"]
            validated_data["height"] = poke_data["height"]
            validated_data["weight"] = poke_data["weight"]
            
        return super().update(instance, validated_data)
