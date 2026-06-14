from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from apps.pokemons.models import Pokemon

class PokemonTests(APITestCase):
    def setUp(self):
        self.url = '/pokemons/'
        self.mock_pokeapi_data = {
            "sprites": {"front_default": "http://example.com/pikachu.png"},
            "height": 4,
            "weight": 60
        }

    @patch('apps.pokemons.serializers.requests.get')
    def test_create_pokemon_success(self, mock_get):
        # Configurar mock
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.mock_pokeapi_data

        data = {"name": "Pikachu"}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pokemon.objects.count(), 1)
        pokemon = Pokemon.objects.get()
        self.assertEqual(pokemon.name, "Pikachu")
        self.assertEqual(pokemon.height, 4)
        self.assertEqual(pokemon.weight, 60)
        self.assertEqual(pokemon.image, "http://example.com/pikachu.png")

    @patch('apps.pokemons.serializers.requests.get')
    def test_create_pokemon_not_found(self, mock_get):
        mock_get.return_value.status_code = 404

        data = {"name": "Inexistente"}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Pokemon.objects.count(), 0)

    @patch('apps.pokemons.serializers.requests.get')
    def test_update_pokemon_fetches_new_data(self, mock_get):
        # Create first
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.mock_pokeapi_data
        
        data = {"name": "Pikachu"}
        create_response = self.client.post(self.url, data, format='json')
        pokemon_id = create_response.data['id']

        # Update to another pokemon
        mock_get.return_value.json.return_value = {
            "sprites": {"front_default": "http://example.com/charmander.png"},
            "height": 6,
            "weight": 85
        }
        update_url = f"{self.url}{pokemon_id}/"
        update_data = {"name": "Charmander"}
        
        response = self.client.patch(update_url, update_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pokemon = Pokemon.objects.get(id=pokemon_id)
        self.assertEqual(pokemon.name, "Charmander")
        self.assertEqual(pokemon.height, 6)
        self.assertEqual(pokemon.weight, 85)
