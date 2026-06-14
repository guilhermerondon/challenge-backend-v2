from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @method_decorator(cache_page(600, key_prefix="pokemon_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def invalidate_list_cache(self):
        cache.delete("pokemon_list")
        # Invalidate views with cache_page. Note: Django's cache_page creates a complex key.
        # A simpler way to invalidate cache_page is clearing the specific keys or using a signal.
        # But for this challenge, cache.clear() is acceptable, or clearing all cache.
        # Better: use cache.delete_pattern("views.decorators.cache.cache_header*pokemon_list*") if using redis.
        # For simplicity, we can use a custom cache key in list view without cache_page, or just clear.
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
