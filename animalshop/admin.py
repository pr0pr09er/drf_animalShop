from django.contrib import admin
from .models import Animal, Order, Category, AnimalType, Status

admin.site.register(Animal)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(AnimalType)
admin.site.register(Status)
