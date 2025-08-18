from rest_framework import serializers
from . import models


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredients
        fields = ['name', 'slug', 'dlc', 'ingredient_image_url', 'spoil_time', 'spoil_time', 'food_quality', 'kcal_per_kg',
                  'source', 'source_image_url']


class RecipeIngredientsSerializer(serializers.ModelSerializer):
    ingredient = IngredientsSerializer(read_only=True)
    recipe = serializers.CharField(source='recipe.name', read_only=True)

    class Meta:
        model = models.RecipeIngredients
        #    fields = ['ingredient', 'ingredient_name', 'amount_required']
        fields = ['recipe', 'ingredient', 'amount_required', 'unit', 'role']


class RecipeONISerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientsSerializer(
        source='recipeingredients_set', many=True, read_only=True
    )

    class Meta:
        model = models.RecipeONI
        fields = ['name', 'description', 'slug', 'image_url', 'dlc', 'food_quality', 'spoil_time', 'kcal_per_kg', 'ingredients', 'source',
                  'source_image_url', 'calories_produced']

