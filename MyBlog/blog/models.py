from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True) # auto_now_add automatically fills it up the time you create the app
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):      # __str__ is important to represent object of the class in proper way 
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name = 'comments', on_delete=models.CASCADE)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    
