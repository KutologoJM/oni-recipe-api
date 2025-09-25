# v3/management/commands/seed_recipes.py

from django.core.management.base import BaseCommand
from faker import Faker
import random

from v3.models import RecipeONI, Ingredients, RecipeIngredients

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with fake RecipeONI data"

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of recipes to create'
        )

    def handle(self, *args, **options):
        count = options['count']
        self.stdout.write(f"Seeding {count} RecipeONI objects...")

        for _ in range(count):
            recipe = RecipeONI.objects.create(
                name=fake.unique.sentence(nb_words=3).replace(".", ""),
                description=fake.text(max_nb_chars=200),
                image_url=fake.image_url(width=200, height=200),
                dlc=fake.lexify(text="?????")[:5],
                food_quality={
                    "Quality": random.choice(["standard", "good", "excellent"]),
                    "Morale impact": f"+{random.randint(0, 5)}"
                },
                spoil_time=random.randint(1, 1000),
                kcal_per_kg=random.randint(100, 1000),
                source=fake.company(),
                source_image_url=fake.image_url(width=200, height=200),
                calories_produced=random.randint(500, 5000),
            )

            # Attach ingredients via RecipeIngredients
            all_ingredients = list(Ingredients.objects.all())
            if all_ingredients:
                chosen_ingredients = random.sample(all_ingredients, random.randint(1, 5))
                for ingredient in chosen_ingredients:
                    RecipeIngredients.objects.create(
                        recipe=recipe,
                        ingredient=ingredient,
                        amount_required=random.randint(1, 10),
                        unit=random.choice(["g", "kg", "ml", "L", "pcs"]),
                        role=random.choice(["main", "alternate"])
                    )

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
