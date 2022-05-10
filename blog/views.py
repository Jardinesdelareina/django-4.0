from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Создавайте свои представления здесь.


def index(request):
    blog = Blog.objects.all()
    return render(request, 'blog/index.html', {'blog': blog, 'title': 'Список записей'})
