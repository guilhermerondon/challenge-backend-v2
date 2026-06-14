from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.trainers.models import Trainer

class TrainerTests(APITestCase):
    def setUp(self):
        self.trainer_data = {"name": "Ash", "age": 10}
        self.trainer = Trainer.objects.create(**self.trainer_data)
        self.url = '/trainers/'

    def test_create_trainer(self):
        data = {"name": "Misty", "age": 12}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trainer.objects.count(), 2)
        self.assertEqual(Trainer.objects.get(id=response.data['id']).name, 'Misty')

    def test_get_trainer_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_trainer(self):
        url = f'{self.url}{self.trainer.id}/'
        data = {"name": "Ash Ketchum", "age": 11}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.trainer.refresh_from_db()
        self.assertEqual(self.trainer.name, "Ash Ketchum")

    def test_delete_trainer(self):
        url = f'{self.url}{self.trainer.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Trainer.objects.count(), 0)
