from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django_filters.views import FilterView
from .models import Recipe, Category, Tag
from.filters import RecipeFilter

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