from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title