from django.db import models

class Article(models.Model):
    content = models.CharField(max_length=200)
    name = models.CharField(max_length=200, null=True)