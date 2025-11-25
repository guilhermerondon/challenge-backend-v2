from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Trainer

class TrainerTests(APITestCase):
    def test_create_trainer(self):
        response = self.client.post("/trainers/", {"name": "Ash", "age": 10})
        self.assertEqual(response.status_code, 201)
