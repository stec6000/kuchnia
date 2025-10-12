from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='')
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='recipes')
    tags = models.ManyToManyField('Tag', related_name='recipes', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

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