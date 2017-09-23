from django.db import models

# Create your models here.
class Tatti(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=20)
    kyu = models.CharField(max_length=30)
    pfft = models.CharField(max_length=10)

    def __str__(self):
        return self.name+' '+self.amount

class Susu(models.Model):
    tatti = models.ForeignKey(Tatti, on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    aroma = models.CharField(max_length=20)