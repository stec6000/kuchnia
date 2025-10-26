from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RecipeListView, RecipeDetailView, RecipeByCategoryView, RecipeByTagView
from .views import RecipeViewSet


app_name = "recipes"
router = DefaultRouter()
router.register(r'api/recipes', RecipeViewSet, basename='recipe')
urlpatterns = [
    
    path("przepisy/", RecipeListView.as_view(), name="recipe_list"),
    path("przepisy/<slug:slug>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("categories/<slug:slug>/", RecipeByCategoryView.as_view(), name="recipe_by_category"),
    path("tags/<slug:slug>/", RecipeByTagView.as_view(), name="recipe_by_tag"),
]

urlpatterns += router.urls