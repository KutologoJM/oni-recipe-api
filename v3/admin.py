from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.RecipeONI)
admin.site.register(models.Ingredients)
admin.site.register(models.RecipeIngredients)
admin.site.register(models.Orders)
admin.site.register(models.FoodOrdersModel)
