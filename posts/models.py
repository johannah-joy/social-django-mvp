from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("posts:home")
    
    def date_today(self):
        self.date_published = timezone.now()
        self.save()

    class Meta:
        ordering = ['-date_published']