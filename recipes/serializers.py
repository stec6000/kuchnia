from rest_framework import serializers
from .models import Recipe, Ingredient, Unit, RecipeIngredient, Category, Tag

class RecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = [
            "id", "title", "slug",
            "prep_time", "servings",
        ]

class IngredientSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ingredient
            fields = ["id", "name", "slug", "kcal_per_100g"]

class UnitSerializer(serializers.ModelSerializer):
        class Meta:
            model = Unit
            fields = ["id", "name", "short_name"]

class RecipeDetailSerializer(serializers.ModelSerializer):

    class CategoryMiniSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ["id", "name", "slug"]
    
    class TagMiniSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = ["id", "name", "slug"]    
    
    class RecipeIngredientReadSerializer(serializers.ModelSerializer):
        ingredient = IngredientSerializer(read_only=True)
        unit = UnitSerializer(read_only=True)
        class Meta:
            model = RecipeIngredient
            fields = ["id", "ingredient", "amount", "unit"]

    ingredients = RecipeIngredientReadSerializer(
        source='recipeingredient_set', many=True, read_only=True
    )
    category = CategoryMiniSerializer(read_only=True)
    tags = TagMiniSerializer(many=True, read_only=True)
    
    class Meta:
        model = Recipe
        fields = [
            "id", "title", "slug",
            "category", "tags",
            "prep_time", "servings",
            "description", "ingredients",
            "instructions",
        ]