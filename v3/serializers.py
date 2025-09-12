from rest_framework import serializers
from . import models


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredients
        fields = ['name', 'description', 'slug', 'dlc', 'ingredient_image_url', 'spoil_time', 'spoil_time',
                  'food_quality',
                  'kcal_per_kg',
                  'source', 'source_image_url']


class RecipeIngredientsSerializer(serializers.ModelSerializer):
    ingredient = IngredientsSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Ingredients.objects.all(),
        source='ingredient',
        write_only=True
    )

    recipe = serializers.CharField(source='recipe.name', read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=models.RecipeONI.objects.all(),
        source='recipe',
        write_only=True
    )

    class Meta:
        model = models.RecipeIngredients
        fields = [
            'recipe', 'recipe_id',
            'ingredient', 'ingredient_id',
            'amount_required', 'unit', 'role'
        ]


class RecipeONISerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientsSerializer(
        source='recipeingredients_set', many=True, read_only=True
    )

    class Meta:
        model = models.RecipeONI
        fields = ['name', 'description', 'slug', 'image_url', 'dlc', 'food_quality', 'spoil_time', 'kcal_per_kg',
                  'ingredients', 'source',
                  'source_image_url', 'calories_produced']




'''
class OrderItemsSerializer(serializers.ModelSerializer):
    order = OrdersSerializer(read_only=True)
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = models.OrderItems
        fields = ["id", "order", "product_name", "quantity"]
'''


class FoodOrderSerializer(serializers.ModelSerializer):
    # Human-readable product name
    product_name = serializers.CharField(source="food_item.name", read_only=True)

    # Accept order ID for writes
    order_id = serializers.PrimaryKeyRelatedField(
        source="order",
        queryset=models.Orders.objects.all(),
        write_only=True
    )

    # Accept food_item ID for writes and takes in RecipeONI primary key as input
    food_item_id = serializers.PrimaryKeyRelatedField(
        source="food_item",
        queryset=models.RecipeONI.objects.all(),
        write_only=True
    )
    order_item_id = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = models.FoodOrdersModel
        fields = [
            "order_item_id",            # always include for updates/deletes
            "order_id",      # write-only
            "food_item_id",  # write-only
            "product_name",  # read-only
            "quantity",
            "category",
        ]


class OrdersSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(
        source="customer",
        queryset=models.User.objects.all(),
        write_only=True
    )
    customer_name = serializers.CharField(
        source="customer.username", read_only=True
    )
    food_orders = FoodOrderSerializer(many=True, read_only=True)
    order_id = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = models.Orders

        fields = [
            "order_id",
            "customer_id",
            "customer_name",
            "status",
            "food_orders"
        ]