from .models import RecipeONI, Ingredients, RecipeIngredients
from rest_framework import generics, filters
from . import serializers

from django_filters.rest_framework import DjangoFilterBackend
from .filters import RecipeONIFilter


class ViewAllRecipes(generics.ListAPIView):
    queryset = RecipeONI.objects.all()
    serializer_class = serializers.RecipeONISerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RecipeONIFilter
    search_fields = ['name', 'dlc']
    ordering_fields = ['spoil_time', 'name']
    ordering = ['name']


class ViewAllIngredients(generics.ListAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = serializers.IngredientsSerializer


class ViewAllRecipeIngredients(generics.ListAPIView):
    queryset = RecipeIngredients.objects.all()
    serializer_class = serializers.RecipeIngredientsSerializer


class ViewChosenRecipe(generics.RetrieveAPIView):
    queryset = RecipeONI.objects.all()
    serializer_class = serializers.RecipeONISerializer
    lookup_field = 'slug'


class ViewChosenIngredient(generics.RetrieveAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = serializers.IngredientsSerializer
    lookup_field = 'slug'
