from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
# Создавайте свои представления здесь.


def index(request):
    blog = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blog': blog, 
        'title': 'Список записей',
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)


def get_category(request, category_id):
    blog = Blog.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'blog': blog,
        'categories': categories,
        'category': category,
    }
    return render(request, 'blog/category.html', context)
