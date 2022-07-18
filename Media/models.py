from django.db import models
from django.utils import timezone


# Create your models here.
class Posts(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField(blank=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.user


class Users(models.Model):
    username = models.CharField(max_length=120, default=f"Random User")
    fullname = models.CharField(max_length=250, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.username
