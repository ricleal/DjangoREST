from django.contrib.auth.models import User
from django.core.validators import validate_slug
from django.db import models
from .validators import validate_acceptable_cost_to_make

# Create your models here.


class Menu(models.Model):

    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=200)
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)

    def __str__(self):
        return '%s by %s %s' % (self.name, self.chef.first_name,
                                self.chef.last_name)


class MenuItem(models.Model):

    # validate
    name = models.CharField(max_length=32, unique=True,
                            validators=[validate_slug])
    description = models.CharField(max_length=200)
    cost_to_make = models.DecimalField(decimal_places=2, max_digits=5,
                                       validators=[validate_acceptable_cost_to_make])
    sale_price = models.DecimalField(decimal_places=2, max_digits=5)
    available = models.BooleanField(default=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return 'Item - %s' % (self.name)
