from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.pokemons.models import Pokemon

class PokemonCreateTests(APITestCase):
    def test_create_pokemon_success(self):
        payload = {"name": "pikachu"}
        response = self.client.post(reverse("pokemon-create"), payload)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Pikachu")
        self.assertTrue("image" in response.data)

    def test_create_pokemon_without_name(self):
        response = self.client.post(reverse("pokemon-create"), {})
        self.assertEqual(response.status_code, 400)

    def test_create_pokemon_invalid(self):
        response = self.client.post(reverse("pokemon-create"), {"name": "xpto-invalido"})
        self.assertEqual(response.status_code, 404)
