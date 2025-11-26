from rest_framework.test import APITestCase
from apps.pokemons.models import Pokemon
from apps.trainers.models import Trainer
from apps.relations.models import TrainerPokemon

class BattleTests(APITestCase):
    def setUp(self):
        self.p1 = Pokemon.objects.create(
            name="Pikachu", image="url", height=4, weight=60
        )
        self.p2 = Pokemon.objects.create(
            name="Bulbasaur", image="url", height=7, weight=69
        )
        self.p3 = Pokemon.objects.create(
            name="Charmander", image="url", height=6, weight=60
        )

        self.trainer = Trainer.objects.create(name="Ash", age=10)

    def test_battle_weight_winner(self):
        response = self.client.get(f"/battle/{self.p1.id}/{self.p2.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["vencedor"], "Bulbasaur")

    def test_battle_draw(self):
        response = self.client.get(f"/battle/{self.p1.id}/{self.p3.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["resultado"], "empate")

    def test_same_trainer_error(self):
        TrainerPokemon.objects.create(trainer=self.trainer, pokemon=self.p1)
        TrainerPokemon.objects.create(trainer=self.trainer, pokemon=self.p2)

        response = self.client.get(f"/battle/{self.p1.id}/{self.p2.id}/")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Pokémons do mesmo treinador", response.data["erro"])

    def test_nonexistent_pokemon(self):
        response = self.client.get("/battle/999/1/")
        self.assertEqual(response.status_code, 404)
