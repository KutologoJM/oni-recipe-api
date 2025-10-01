from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'recipes', RecipesViewSet, basename='recipes')
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')
router.register(r'recipe-ingredients', RecipeIngredientsViewSet, basename='recipe-ingredients')
# router.register(r'orders', OrdersViewSet, basename='orders')
# router.register(r'food-orders', FoodManagerViewSet, basename='order-items')
# router.register(r'', viewset, basename='basename')
urlpatterns = router.urls
