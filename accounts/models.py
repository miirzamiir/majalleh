from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    age = models.IntegerField(blank=True)
    photo = models.ImageField(null=True, upload_to='users/%Y/%m/%d')
    bio = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.user.username
