# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Define the Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Define the Car Model model
class CarModel(models.Model):
    # Choices for car type
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('Truck', 'Truck'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Hatchback', 'Hatchback')
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.car_make.name} {self.car_type} {self.name} ({self.year})"

