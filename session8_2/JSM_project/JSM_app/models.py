from django.contrib.auth.models import User
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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', default=1)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomments')
    body = models.TextField()

    def __str__(self):
        return self.body