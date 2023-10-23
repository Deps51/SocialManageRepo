from django.db import models

# Create your models here.

class Media(models.Model):
    media = models.FileField()