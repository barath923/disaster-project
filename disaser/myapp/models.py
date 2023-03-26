from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    collector = 1
    admin = 2
    ROLE_CHOICES = (
        (collector,'collector'),
        (admin,'admin')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,null=True,blank=True)

class officer(models.Model):
    ref=models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='man')

    class Meta:
        db_table='officer'