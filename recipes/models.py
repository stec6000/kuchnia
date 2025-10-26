from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, default='')
    kcal_per_100g = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.short_name
    
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='')
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    instructions = models.TextField()
    prep_time = models.TextField(max_length=10, blank=True)
    servings = models.IntegerField(null=True, blank=True)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='recipes')
    tags = models.ManyToManyField('Tag', related_name='recipes', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.ingredient.name} {self.amount} {self.unit} in {self.recipe.title}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name