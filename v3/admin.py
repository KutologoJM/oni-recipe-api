from django.contrib import admin
from django.apps import apps
from . import models

# Register your models here.
"""
admin.site.register(models.RecipeONI)
admin.site.register(models.Ingredients)
admin.site.register(models.RecipeIngredients)
admin.site.register(models.Orders)
admin.site.register(models.FoodOrders)
admin.site.register(models)
"""

app = apps.get_app_config('v3')

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
