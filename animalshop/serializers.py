from rest_framework import serializers
from animalshop.models import Animal, Order


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
