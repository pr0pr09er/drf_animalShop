from django.db import models

choises = [
    ('выполнен', 'completed'),
    ('размещен', 'posted'),
    ('обработан', 'processed'),
]


class Animal(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='animalshop/img/')
    animal_type = models.ForeignKey("AnimalType", on_delete=models.CASCADE)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)


class AnimalType(models.Model):
    name = models.CharField(max_length=255)


class Status(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    pet_info = models.ManyToManyField("Animal")
    count = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=choises, max_length=30)
