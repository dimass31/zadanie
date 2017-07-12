from django.db import models

class String(models.Model):
    string = models.CharField(max_length=128)