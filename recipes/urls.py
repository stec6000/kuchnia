from django.urls import path
from .views import recipe_list

urlpatterns = [
    path("przepisy/", recipe_list, name='recipe_list'),
]