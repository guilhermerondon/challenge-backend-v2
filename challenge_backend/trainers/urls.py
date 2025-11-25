from django.urls import path
from .views import TrainerListCreateView, TrainerDetailView

urlpatterns = [
    path('', TrainerListCreateView.as_view()),
    path('<int:pk>/', TrainerDetailView.as_view()),
]
