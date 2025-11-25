from rest_framework import generics
from .models import Trainer
from .serializers import TrainerSerializer

class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
