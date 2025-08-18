from django.urls import path
from . import views

urlpatterns = [
    path("view/recipes/", views.ViewAllRecipes.as_view()),
    path('view/recipes/<slug:slug>/', views.ViewChosenRecipe.as_view()),
    path('view/ingredients/', views.ViewAllIngredients.as_view()),
    path('view/ingredients/<slug:slug>/', views.ViewChosenIngredient.as_view()),
    path('view/all-recipe-ingredients/', views.ViewAllRecipeIngredients.as_view()),
]
