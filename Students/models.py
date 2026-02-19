from django.db import models

class student(models.Model):
    
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
