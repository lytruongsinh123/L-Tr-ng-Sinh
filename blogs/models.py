from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True)
    video = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)



class CustomUser(AbstractUser):
    # Add your custom fields here
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username