from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Buyer(models.Model):
    name = models.CharField(max_length=80)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    size = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
