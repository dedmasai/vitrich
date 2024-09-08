from django.db import models

# Create your models here.
class Plants(models.Model):
    title = models.CharField(max_length=255)
    titleL = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    maxPoints=models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Team(models.Model):
    title = models.CharField(max_length=255)
    school=models.CharField(max_length=255)
    points=models.IntegerField(default=0)
    expert=models.ForeignKey('Expert', on_delete=models.PROTECT,default=None)
    plants = models.ManyToManyField(Plants, through="CheckList",related_name='team')

    # Categories
    CATEGORIES = (
        ('РВ', 'Разновозрастные'),
        ('В', 'Взрослые'),
        ('Э', 'Эксперты'),
        ('М', 'Младшие школьники'),
    )

    category = models.CharField(max_length=300, choices=CATEGORIES, default=None)

    def __str__(self):
        return self.title

class Expert(models.Model):
    name = models.CharField(max_length=255)
    phone =models.CharField(max_length=255,default=None)

    def __str__(self):
        return self.name



class CheckList(models.Model): #https://metanit.com/python/django/5.7.php
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    points = models.IntegerField()
