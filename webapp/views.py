from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bienvenido(request):
    return HttpResponse('Hola mundo')

def contacto(request):
    return HttpResponse('tel: email:')