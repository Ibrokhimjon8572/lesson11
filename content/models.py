from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISH = 'PB', 'Publish'

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISH)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-updated']

class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(default='defaultpostimg.png')