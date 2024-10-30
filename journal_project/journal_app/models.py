from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mood(models.Model):
    mood = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.mood)
    
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    mood = models.ForeignKey(Mood, null=True, on_delete=models.SET_NULL)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return str(self.title)

