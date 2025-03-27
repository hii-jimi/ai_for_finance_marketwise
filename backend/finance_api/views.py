from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello_backend(request):
    data = {'message': 'Hello from the Django backend!'}
    return JsonResponse(data)