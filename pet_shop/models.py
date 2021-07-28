from django.db import models
from django.db.models.deletion import CASCADE


class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)


class Characteristic(models.Model):
    name = models.CharField(max_length=255)
