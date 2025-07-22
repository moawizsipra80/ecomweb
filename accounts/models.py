from django.utils import timezone
from django.db import models
class User(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=50,default='')
    password=models.CharField(max_length=50,default='')
    contactno=models.CharField(max_length=19,default='')
    def __str__(self):
        return self.name
# Create your models here.
