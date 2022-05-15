from msilib.schema import ListView
from .models import Blog, Category
from .forms import BlogForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/add_note.html'
    success_url = reverse_lazy('home')   # Выполняет функцию redirect
    