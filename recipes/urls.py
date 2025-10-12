from django.urls import path
from .views import RecipeListView, RecipeDetailView

app_name = "recipes"

urlpatterns = [
    
    path("przepisy/", RecipeListView.as_view(), name="recipe_list"),
    path("przepisy/<slug:slug>/", RecipeDetailView.as_view(), name="recipe_detail"),
]