from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user)
admin.site.register(restaurant_details)
admin.site.register(dish)
admin.site.register(rest_dish_map)
