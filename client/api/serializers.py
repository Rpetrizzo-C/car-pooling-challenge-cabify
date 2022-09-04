from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    car_id = serializers.IntegerField()
    seats = serializers.IntegerField()

class LocationSerializer(serializers.Serializer):
    group = serializers.IntegerField()
    car = serializers.IntegerField()
