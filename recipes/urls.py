from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeByCategoryView, RecipeByTagView

app_name = "recipes"

urlpatterns = [
    
    path("przepisy/", RecipeListView.as_view(), name="recipe_list"),
    path("przepisy/<slug:slug>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("categories/<slug:slug>/", RecipeByCategoryView.as_view(), name="recipe_by_category"),
    path("tags/<slug:slug>/", RecipeByTagView.as_view(), name="recipe_by_tag"),
]