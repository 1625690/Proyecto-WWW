from django.db import models

# Create your models here.


class Electricaribe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()