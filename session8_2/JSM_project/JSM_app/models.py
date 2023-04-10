from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_post = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateTimeField(null = True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title