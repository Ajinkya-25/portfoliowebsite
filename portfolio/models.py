from django.db import models

# Create your models here.
class product(models.Model):
    name=models.TextField()
    summary=models.TextField(default='hi there')
