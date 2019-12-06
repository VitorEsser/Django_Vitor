from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural =  'Marcas'

    def __str__(self):
        return self.name

class Instrument(models.Model):
    name = models.CharField(max_length=100)    
    brands = models.ManyToManyField(Brand, related_name='instrument_brand')
    strings = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='instrument', blank=True, null=True)

    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'

    def __str__(self):
        return str(self.name)

    @property
    def get_brands(self):
        brands = [x for x in self.brands.all()]
        return brands