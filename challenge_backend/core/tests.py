from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Trainer, Pokemon, TrainerPokemon

class TrainerTests(APITestCase):

  def test_create_trainer(self):
      url = '/api/trainers/'
      data = {'name': 'Ash Ketchum', 'age': 10}
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(response.data['name'], 'Ash Ketchum')

  def teste_list_trainers(self):
      Trainer.objects.create(name='Misty', age=12)
      Trainer.objects.create(name='Brock', age=15)
      url = '/api/trainers/'
      response = self.client.get(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 2)

class PokemonTests(APITestCase):

  def test_create_pokemon(self):
      url = '/api/pokemons/'
      data = {
         'name': 'Pikachu', 
         'photo': 'http://example.com/pikachu.png', 
         'height': 4, 
         'weight': 60
         }
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(response.data['name'], 'Pikachu')

  def test_list_pokemons(self):
      Pokemon.objects.create(name='Bulbasaur', photo='http://example.com/bulbasaur.png', height=7, weight=69)
      Pokemon.objects.create(name='Charmander', photo='http://example.com/charmander.png', height=6, weight=85)
      url = '/api/pokemons/'
      response = self.client.get(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 2)

# Create your tests here.
class TrainerPokemonTests(APITestCase):

  def setUp(self):
      self.trainer = Trainer.objects.create(name='Ash Ketchum', age=10)
      self.p1 = Pokemon.objects.create(name='Pikachu', photo='http://example.com/pikachu.png', height=4, weight=60)
      self.p2 = Pokemon.objects.create(name='Squirtle', photo='http://example.com/squirtle.png', height=5, weight=90)

  def test_add_pokemon_to_trainer(self):
      url = '/api/trainer-pokemons/'
      data = {'trainer': self.trainer.id, 'pokemon': self.p1.id}
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(TrainerPokemon.objects.count(), 1 )

  def test_remove_pokemon_from_trainer(self):
      relation = TrainerPokemon.objects.create(trainer=self.trainer, pokemon=self.p1)

      url = f'/api/trainer-pokemons/{relation.id}/'
      response = self.client.delete(url, format='json')

      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertEqual(TrainerPokemon.objects.count(), 0)

class PokemonBattleTests(APITestCase):

  def setUp(self):
      self.trainer1 = Trainer.objects.create(name='Ash Ketchum', age=10)
      self.trainer2 = Trainer.objects.create(name='Misty', age=12)

      self.p1 = Pokemon.objects.create(name='Pikachu', photo='http://example.com/pikachu.png', height=4, weight=60)
      self.p2 = Pokemon.objects.create(name='Squirtle', photo='http://example.com/squirtle.png', height=5, weight=90)

      TrainerPokemon.objects.create(trainer=self.trainer1, pokemon=self.p1)
      TrainerPokemon.objects.create(trainer=self.trainer2, pokemon=self.p2)

  def test_pokemon_battle(self):
      url = f'/api/battle/{self.p1.id}/{self.p2.id}/'
      response = self.client.get(url, format='json')

      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertIn('Vencedor', response.data)
      self.assertIn('Derrotado', response.data)

  def test_pokemon_battle_same_trainer(self):
      TrainerPokemon.objects.create(trainer=self.trainer1, pokemon=self.p2)

      url = f'/api/battle/{self.p1.id}/{self.p2.id}/'
      response = self.client.get(url, format='json')

      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      self.assertIn(response.data['error'], "Os Pokémons pertencem ao mesmo treinador.")

class PokeAPITests(APITestCase):
   
   def test_invalid_pokemon(self):
       url = '/api/pokeapi/pokemoninexistente/'
       response = self.client.get(url, format='json')
       self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       self.assertIn('error', response.data)