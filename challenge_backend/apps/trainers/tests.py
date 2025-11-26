from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.trainers.models import Trainer


class TrainerTests(APITestCase):

    def setUp(self):
        self.trainer_data = {"name": "Ash", "age": 10}
        self.trainer = Trainer.objects.create(name="Misty", age=12)

    # CREATE
    def test_create_trainer(self):
        response = self.client.post("/trainers/", self.trainer_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Ash")

    # LIST
    def test_list_trainers(self):
        response = self.client.get("/trainers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    # RETRIEVE
    def test_get_trainer_by_id(self):
        response = self.client.get(f"/trainers/{self.trainer.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.trainer.name)

    # UPDATE
    def test_update_trainer(self):
        update_data = {"name": "Misty Updated", "age": 13}
        response = self.client.put(f"/trainers/{self.trainer.id}/", update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Misty Updated")

    # DELETE
    def test_delete_trainer(self):
        response = self.client.delete(f"/trainers/{self.trainer.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Trainer.objects.filter(id=self.trainer.id).exists())
