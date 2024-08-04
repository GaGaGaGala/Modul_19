from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=80)
    balance = models.DecimalField(decimal_places=4, max_digits=4)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=3, max_digits=3)
    size = models.DecimalField(decimal_places=4, max_digits=4)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
