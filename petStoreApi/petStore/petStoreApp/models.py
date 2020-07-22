from django.db import models

# Create your models here.
class Animal(models.Model):
    COLORS = [
        ('RED', 'Red'),
        ('BLUE', 'Blue'),
        ('BROWN', 'Brown'),
        ('BLACK', 'Black'),
        ('WHITE', 'White'),
    ]
    arrival = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length= 5, choices= COLORS)
    name = models.CharField(max_length= 30, blank= True)
    
    class Meta:
        abstract = True

class Dog(Animal):
    BREEDS = [
        ('GS', 'German Shepherd'),
        ('BD', 'Bulldog'),
        ('PD', 'Poodle'),
        ('GD', 'Golden Retriever'),
        ('BG', 'Beagle'),
        ('CH', 'Chihuahua'),
    ]
    breed = models.CharField(max_length= 2, choices= BREEDS)

class Cat(Animal):
    BREEDS = [
        ('PS', 'Persian'),
        ('BC', 'Bengal'),
        ('SM', 'Siamese'),
        ('RD', 'Ragdoll')
    ]
    breed = models.CharField(max_length= 2, choices= BREEDS)

class Fish(Animal):
    BREEDS = [
        ('K', 'Koi'),
        ('O', 'Oranda'),
        ('C', 'Comet'),
        ('BT', 'Black Telescope'),
        ('F', 'Fantail'),
    ]
    breed = models.CharField(max_length= 2, choices= BREEDS)

class User(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(unique= True)
    
class Admin(User):
    password = models.CharField(max_length= 30)
        