from rest_framework import status
from rest_framework.test import APITestCase
from apps.trainers.models import Trainer
from apps.pokemons.models import Pokemon
from apps.relations.models import TrainerPokemon

class RelationTests(APITestCase):
    def setUp(self):
        self.trainer = Trainer.objects.create(name="Ash", age=10)
        self.pokemon = Pokemon.objects.create(
            name="Pikachu", image="img", height=4, weight=60
        )
        self.add_url = reverse('add_pokemon')
        self.remove_url = reverse('remove_pokemon')

    def test_add_pokemon_to_trainer(self):
        data = {"trainer_id": self.trainer.id, "pokemon_id": self.pokemon.id}
        response = self.client.post(self.add_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TrainerPokemon.objects.count(), 1)

    def test_prevent_duplicate_pokemon_for_trainer(self):
        TrainerPokemon.objects.create(trainer=self.trainer, pokemon=self.pokemon)
        
        data = {"trainer_id": self.trainer.id, "pokemon_id": self.pokemon.id}
        response = self.client.post(self.add_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_remove_pokemon_from_trainer(self):
        TrainerPokemon.objects.create(trainer=self.trainer, pokemon=self.pokemon)
        
        data = {"trainer_id": self.trainer.id, "pokemon_id": self.pokemon.id}
        response = self.client.delete(self.remove_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TrainerPokemon.objects.count(), 0)
