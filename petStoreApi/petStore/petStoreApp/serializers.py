from rest_framework import serializers
from petStoreApp.models import Animal, Cat, Dog, Fish

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    name = serializers.CharField(required= False)
    color = serializers.CharField()
    arrival = serializers.DateTimeField(read_only= True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.arrival = validated_data.get('arrival', instance.arrival)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.save()
        return instance

class DogSerializer(AnimalSerializer):
    breed = serializers.CharField()

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)

class CatSerializer(AnimalSerializer):
    breed = serializers.CharField()

    def create(self, validated_data):
        return Cat.objects.create(**validated_data)

class FishSerializer(AnimalSerializer):
    breed = serializers.CharField()

    def create(self, validated_data):
        return Fish.objects.create(**validated_data)

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only= True)
    name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class AdminSerializer(UserSerializer):
    password = serializers.CharField(write_only= True)

    def create(self, validated_data):
        return Admin.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance