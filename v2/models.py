from django.db import models
from django.utils.text import slugify


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    dlc = models.CharField(max_length=5)
    ingredient_image_url = models.URLField(max_length=100, blank=True)
    spoil_time = models.IntegerField()
    food_quality = models.JSONField()
    kcal_per_kg = models.IntegerField()
    source = models.CharField(max_length=50)
    source_image_url = models.URLField(max_length=100, blank=True)
    slug = models.SlugField(unique=False, null=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecipeONI(models.Model):
    name = models.CharField(unique=True, default='Placeholder', max_length=50)
    description = models.TextField(null=True, max_length=200)
    image_url = models.URLField(max_length=100, blank=True)
    dlc = models.CharField(max_length=5)
    food_quality = models.JSONField()
    spoil_time = models.IntegerField()
    kcal_per_kg = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredients', through='RecipeIngredients', related_name='recipes')
    source = models.CharField(max_length=50)
    source_image_url = models.URLField(max_length=100, blank=True)
    calories_produced = models.IntegerField()
    slug = models.SlugField(unique=False, null=True)

    class Meta:
        verbose_name = "ONI Recipe"
        verbose_name_plural = "ONI Recipes"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    ROLE_CHOICES = [
        ('main', 'Main'),
        ('alternate', 'Alternate')
    ]
    recipe = models.ForeignKey(RecipeONI, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    amount_required = models.IntegerField()
    unit = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    class Meta:
        verbose_name = "Recipe Ingredients"
        verbose_name_plural = "Recipe Ingredients"

    def __str__(self):
        return f"{self.amount_required} {self.unit} of {self.ingredient.name} for {self.recipe.name}"
