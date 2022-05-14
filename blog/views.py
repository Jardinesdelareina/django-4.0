from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from .forms import BlogForm

# Создавайте свои представления здесь.


def index(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog, 
        'title': 'Список записей',
    }
    return render(request, 'blog/index.html', context)


def get_category(request, category_id):
    blog = Blog.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'blog': blog,
        'category': category,
    }
    return render(request, 'blog/category.html', context)


def get_note(request, note_id):
    view_note = get_object_or_404(Blog, pk=note_id)
    context = {
        'view_note': view_note,
    }
    return render(request, 'blog/note.html', context)


def add_note(request):
    if request.method == 'POST':
        pass
    else:
        form = BlogForm()

    context = {
        'form': form
    }
    return render(request, 'blog/add_note.html', context)