from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.


class RecipesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeONISerializer
    queryset = models.RecipeONI.objects.all()


class IngredientsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientsSerializer
    queryset = models.Ingredients.objects.all()


class RecipeIngredientsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeIngredientsSerializer
    queryset = models.RecipeIngredients.objects.all()


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrdersSerializer
    queryset = models.Orders.objects.all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


'''
class OrderItemsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderItemsSerializer
    queryset = models.OrderItems.objects.all()
'''


class FoodManagerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FoodOrderSerializer
    queryset = models.FoodOrders.objects.all()
