from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from petStoreApp.models import *
from petStoreApp.serializers import *

def get_serializer(animal):
    serializerObj = None
    animalObj = None
    if animal == "dogs":
        serializerObj = DogSerializer
        animalObj = Dog
    elif animal == "cats":
        serializerObj = CatSerializer
        animalObj = Cat
    elif animal == "fish":
        serializerObj = FishSerializer
        animalObj = Fish
    return serializerObj, animalObj


# Create your views here.
@csrf_exempt
def animal_list(request, animal):
    serializerObj, animal = get_serializer(animal)
    if request.method == 'GET':
        animals = animal.objects.all()
        serializer = serializerObj(animals, many= True)
        return JsonResponse(serializer.data, safe= False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializerObj(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status= 400)

@csrf_exempt
def animal_detail(request, animal, pk):
    try:
        current_animal = animal.objects.get(pk= pk)
    except animal.DoesNotExist:
        return HttpResponse(status= 404)

    serializerObj, animal = get_serializer(animal)
    if request.method == 'GET':
        serializer = serializerObj(current_animal)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = serializerObj(current_animal, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.erros, status= 400)
    elif request.method == 'DELETE':
        current_animal.delete()
        return HttpResponse(status= 204)

@csrf_exempt
def user_list(request, admin= False):
    serializerObj = UserSerializer
    person = User
    if admin:
        serializerObj = AdminSerializer
        person = Admin
    if request.method == 'GET':
        users = person.objects.all()
        serializer = serializerObj(users, many= True)
        return JsonResponse(serializer.data, safe= False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializerObj(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status= 400)

@csrf_exempt
def user_detail(request, pk, admin= False):
    serializerObj = UserSerializer
    person = User
    if admin:
        serializerObj = AdminSerializer
        person = Admin
    try:
        user = person.objects.get(pk= pk)
    except person.DoesNotExist:
        return HttpResponse(status= 404)
    
    if request.method == 'GET':
        serializer = serializerObj(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = serializerObj(user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.erros, status= 400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status= 204)

def user_only_list(request):
    return user_list(request)

def admin_list(request):
    return user_list(request, admin= True)

def user_only_detail(request, pk):
    return user_detail(request, pk)

def admin_detail(request, pk):
    return user_detail(request, pk, admin= True)

# @csrf_exempt
# def all_animals(request):
#     if request.method == 'GET':
#         dogs = Dog.objects.all()
#         cats = Cat.objects.all()
#         fish = Fish.objects.all()
#         dog_serializer = DogSerializer(dogs, many=True)
#         cat_serializer = CatSerializer(cats, many= True)
#         fish_serializer = FishSerializer(fish, many= True)
#         data = [dog_serializer, ]