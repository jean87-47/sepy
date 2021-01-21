from django.db import models

# Create your models here.

class Key(models.Model):
    key=models.CharField(max_length=140)
