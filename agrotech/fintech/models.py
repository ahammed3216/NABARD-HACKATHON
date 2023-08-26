from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Announcement(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    image=models.ImageField()