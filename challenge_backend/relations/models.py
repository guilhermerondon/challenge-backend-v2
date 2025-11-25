from django.db import models
from trainers.models import Trainer
from pokemons.models import Pokemon

class TrainerPokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('trainer', 'pokemon')