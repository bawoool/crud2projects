from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=400)
    age = models.IntegerField()

    class Meta:
        db_table = 'owner'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    class Meta:
        db_table = 'dog'