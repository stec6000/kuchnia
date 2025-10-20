import django_filters
from django.db.models import Q
from .models import Recipe, Tag, Category
from django import forms

class RecipeFilter(django_filters.FilterSet):

    search = django_filters.CharFilter(
        method='filter_by_all_fields',
        label="Szukaj"
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="Kategoria",
        empty_label="Wszystkie"
    )

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Tagi"
    )

    class Meta:
        model = Recipe
        fields = ["category", "tags", "search"]

    def filter_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(slug__icontains=value) |
            Q(ingredients__icontains=value) |
            Q(description__icontains=value)
        )