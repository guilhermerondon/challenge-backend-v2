from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import Trainer
from .serializers import TrainerSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    @method_decorator(cache_page(600, key_prefix="trainer_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def invalidate_list_cache(self):
        cache.clear()

    def perform_create(self, serializer):
        serializer.save()
        self.invalidate_list_cache()

    def perform_update(self, serializer):
        serializer.save()
        self.invalidate_list_cache()

    def perform_destroy(self, instance):
        instance.delete()
        self.invalidate_list_cache()
