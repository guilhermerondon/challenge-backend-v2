from rest_framework.test import APITestCase
from apps.trainers.models import Trainer
from apps.pokemons.models import Pokemon
from apps.relations.models import TrainerPokemon

class TrainerPokemonRelationTests(APITestCase):
    def setUp(self):
        self.trainer = Trainer.objects.create(name="Ash", age=10)
        self.pokemon = Pokemon.objects.create(
            name="Pikachu", image="url", height=4, weight=60
        )

    def test_add_pokemon_to_trainer(self):
        response = self.client.post(
            "/relations/add/",
            {"trainer_id": self.trainer.id, "pokemon_id": self.pokemon.id}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(TrainerPokemon.objects.count(), 1)

    def test_add_pokemon_invalid_trainer(self):
        response = self.client.post(
            "/relations/add/",
            {"trainer_id": 999, "pokemon_id": self.pokemon.id}
        )
        self.assertEqual(response.status_code, 404)

    def test_remove_pokemon_from_trainer(self):
        TrainerPokemon.objects.create(
            trainer=self.trainer,
            pokemon=self.pokemon
        )

        response = self.client.delete(
            "/relations/remove/",
            {"trainer_id": self.trainer.id, "pokemon_id": self.pokemon.id},
            format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TrainerPokemon.objects.count(), 0)

    def test_remove_nonexistent_relation(self):
        response = self.client.delete(
            "/relations/remove/",
            {"trainer_id": self.trainer.id, "pokemon_id": self.pokemon.id},
            format="json"
        )
        self.assertEqual(response.status_code, 404)
