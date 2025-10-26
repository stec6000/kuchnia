from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch
from django_filters.views import FilterView
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import RecipeSerializer, RecipeDetailSerializer
from .models import Recipe, Category, Tag, RecipeIngredient
from.filters import RecipeFilter

class RecipeViewSet(ReadOnlyModelViewSet):
    queryset = (
    Recipe.objects.all()
    .order_by("-created_at")
    .select_related("category")
    .prefetch_related(
        "tags",
        Prefetch(
            "recipeingredient_set",
            queryset=RecipeIngredient.objects.select_related("ingredient", "unit").order_by("id"),
        ),
    )
)
    serializer_class = RecipeSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeDetailSerializer
        return RecipeSerializer

class RecipeListView(FilterView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    filterset_class = RecipeFilter
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'recipe'

class RecipeByCategoryView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        return Recipe.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
class RecipeByTagView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs['slug'])
        return Recipe.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context