from msilib.schema import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category
from .forms import BlogForm
from django.views.generic import ListView, DetailView

# Создавайте свои представления здесь.

class BlogView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog'    # Имя, по которому мапятся данные в шаблоне через цикл for


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все записи'
        return context


    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogCategory(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog'
    allow_empty = False


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/note.html'
    context_object_name = 'view_note'



def add_note(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # note = Blog.objects.create(**form.cleaned_data)   # Форма не связана с моделью
            note = form.save()  # Форма связана с моделью
            return redirect(note)
    else:
        form = BlogForm()

    context = {
        'form': form
    }
    return render(request, 'blog/add_note.html', context)