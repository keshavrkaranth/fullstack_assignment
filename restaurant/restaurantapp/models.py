from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.BigIntegerField()

    def __str__(self):
        return self.user.username


class restaurant_details(models.Model):
    Name = models.CharField(max_length=50)
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class dish(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='dishimg/%y-%m-%d')

    def __str__(self):
        return self.name


class rest_dish_map(models.Model):
    restaurant = models.ForeignKey(
        'restaurant_details', on_delete=models.CASCADE)
    dishes = models.ManyToManyField('dish')

    def __str__(self):
        return f'{self.restaurant.Name} this hotel has {self.dishes.count()} dish'
