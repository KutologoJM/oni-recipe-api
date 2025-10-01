from rest_framework import viewsets
from . import models
from . import serializers
from accounts.permissions import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class RecipesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeONISerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return models.RecipeONI.objects.all()
        return models.RecipeONI.objects.filter(creator=user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class IngredientsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return models.Ingredients.objects.all()
        return models.Ingredients.objects.filter(creator=user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RecipeIngredientsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeIngredientsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return models.RecipeIngredients.objects.all()
        return models.RecipeIngredients.objects.filter(creator=user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrdersSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = models.Orders.objects.all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


'''
class OrderItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = serializers.OrderItemsSerializer
    queryset = models.OrderItems.objects.all()
'''


class FoodManagerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    serializer_class = serializers.FoodOrderSerializer
    queryset = models.FoodOrders.objects.all()
