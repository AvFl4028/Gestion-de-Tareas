from django.db import models


# Create your models here.
class TestDb(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
