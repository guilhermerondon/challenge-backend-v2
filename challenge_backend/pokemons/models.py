from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()
    height = models.IntegerField()
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
