from datetime import date
from django.db import models

# Create your models here.


class Note(models.Model):
    """  
    id
    note
    date
    user"""
    #id=models.AutoField(auto_created = True)
    note=models.CharField(max_length=500)
    user=models.CharField(max_length=20)


