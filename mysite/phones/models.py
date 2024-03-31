from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    discription = models.CharField(max_length=100)

    def _str_(self):
     return self.name
