from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Create(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 100)
    tags = models.CharField(max_length = 100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.title

    def show(self):
        return self.content[:3]

class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    confirm = models.CharField(max_length = 100)

    def __str__(self):
        self.last_name