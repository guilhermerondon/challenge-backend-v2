from rest_framework import status
from rest_framework.test import APITestCase
from apps.trainers.models import Trainer
from apps.pokemons.models import Pokemon
from apps.relations.models import TrainerPokemon

class BattleTests(APITestCase):
    def setUp(self):
        self.trainer1 = Trainer.objects.create(name="Ash", age=10)
        self.trainer2 = Trainer.objects.create(name="Gary", age=10)
        
        self.pika = Pokemon.objects.create(name="Pikachu", weight=60)
        self.snorlax = Pokemon.objects.create(name="Snorlax", weight=4600)
        self.ditto = Pokemon.objects.create(name="Ditto", weight=60) # Same weight as pika

    def test_battle_different_weights(self):
        url = f'/battle/{self.pika.id}/{self.snorlax.id}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["vencedor"], "Snorlax")

    def test_battle_same_weight_tie(self):
        url = f'/battle/{self.pika.id}/{self.ditto.id}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["resultado"], "empate")

    def test_battle_same_team_error(self):
        TrainerPokemon.objects.create(trainer=self.trainer1, pokemon=self.pika)
        TrainerPokemon.objects.create(trainer=self.trainer1, pokemon=self.snorlax)
        
        url = f'/battle/{self.pika.id}/{self.snorlax.id}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("erro", response.data)
