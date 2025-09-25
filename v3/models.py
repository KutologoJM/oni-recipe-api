from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, max_length=200)
    dlc = models.CharField(max_length=5)
    ingredient_image_url = models.URLField(max_length=100, blank=True)
    spoil_time = models.IntegerField()
    food_quality = models.JSONField(help_text='{"Quality": "standard", "Morale impact": "+0"}')
    kcal_per_kg = models.IntegerField()
    source = models.CharField(max_length=50)
    source_image_url = models.URLField(max_length=100, blank=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name


class RecipeONI(models.Model):
    name = models.CharField(unique=True, default='Placeholder', max_length=50)
    description = models.TextField(null=True, max_length=200)
    image_url = models.URLField(max_length=100, blank=True)
    dlc = models.CharField(max_length=5)
    food_quality = models.JSONField(help_text='{"Quality": "standard", "Morale impact": "+0"}')
    spoil_time = models.IntegerField()
    kcal_per_kg = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredients', through='RecipeIngredients', related_name='recipes')
    source = models.CharField(max_length=50)
    source_image_url = models.URLField(max_length=100, blank=True)
    calories_produced = models.IntegerField()
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        verbose_name = "ONI Recipe"
        verbose_name_plural = "ONI Recipes"

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    ROLE_CHOICES = [
        ('main', 'Main'),
        ('alternate', 'Alternate')
    ]
    recipe = models.ForeignKey(RecipeONI, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    amount_required = models.PositiveIntegerField()
    unit = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    class Meta:
        verbose_name = "Recipe Ingredients"
        verbose_name_plural = "Recipe Ingredients"

    def __str__(self):
        return f"{self.amount_required} {self.unit} of {self.ingredient.name} for {self.recipe.name}"


class Orders(models.Model):
    ORDER_STATUS = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="pending", help_text="Pending, Completed or Canceled")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.id} status: {self.status}"


'''
class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(RecipeONI, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=30, default=food)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"Order no. {self.id}"
'''


class BaseOrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=30)

    class Meta:
        abstract = True


class ONIElements(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, max_length=200)
    dlc = models.CharField(max_length=5)


class ONIBuildings(models.Model):
    pass


class FoodOrders(BaseOrderItem):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="food_orders")
    food_item = models.ForeignKey(RecipeONI, on_delete=models.CASCADE, related_name="food_order_item")

    class Meta:
        verbose_name = "Food order item"
        verbose_name_plural = "Food order items"

    def __str__(self):
        return f"{self.quantity} × {self.food_item.name} (Order {self.order.id})"


class ElementOrders(BaseOrderItem):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="element_orders")
    element_item = models.ForeignKey(ONIElements, on_delete=models.CASCADE, related_name="element_order_item")

    class Meta:
        verbose_name = "Element order item"
        verbose_name_plural = "Element order items"

    def __str__(self):
        return f"{self.element_item}"


class BuildingOrders(BaseOrderItem):
    building = models.ForeignKey(ONIBuildings, on_delete=models.CASCADE, related_name="building_order_item")

    class Meta:
        verbose_name = "Building order item"
        verbose_name_plural = "Building order items"

    def __str__(self):
        return f"{self.building}"
