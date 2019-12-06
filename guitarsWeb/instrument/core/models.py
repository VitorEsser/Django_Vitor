from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instrument(models.Model):
    name = models.CharField(max_length=100)    
    brand = models.CharField(max_length=100)
    strings = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='instrument', blank=True, null=True)
    
    def __str__(self):
        return str(self.name)