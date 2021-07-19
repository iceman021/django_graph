from django.db import models


# Create your models here.
class Products(models.Model):

    COLOR = (
        ("WHITE", 'White'),
        ("GOLD", 'Gold'),
        ("BLUE", 'Blue'),
        ("GREEN", 'Green'),
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=COLOR)
    price = models.IntegerField()

    def __str__(self):
        return '{}: - {}: - {}:'.format(self.name, self.color, self.price)