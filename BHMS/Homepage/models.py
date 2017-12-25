from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.name

class userProfile(models.Model):
    u_profile = models.OneToOneField(User,unique=True)
    room_no = models.IntegerField()
    def __str__(self):
        return self.u_profile.username