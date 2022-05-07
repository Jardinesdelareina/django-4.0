from django.shortcuts import render
from django.http import HttpResponse

# Создавайте свои представления здесь.

def index(request):
    return HttpResponse('Hello World')


def test(request):
    return HttpResponse('<h1>Hola amigo!</h1>')
