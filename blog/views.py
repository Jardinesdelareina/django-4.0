from django.shortcuts import redirect, render
from .models import Blog, Category
from .forms import BlogForm, UserRegisterForm, UserAuthForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import UpperMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages

# Создавайте свои представления здесь.


class BlogView(UpperMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog'    # Имя, по которому мапятся данные в шаблоне через цикл for
    mixin_prop = 'добро пожаловать'
    paginate_by = 3   # Пагинация, количество записей на странице     


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context


    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('category')    # Используется при ForeignKey в модели для сокращения SQL-запросов на странице


class BlogCategory(UpperMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blog'
    allow_empty = False
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context


    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/note.html'
    context_object_name = 'view_note'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/add_note.html'
    success_url = reverse_lazy('home')   # Выполняет функцию redirect
    login_url = '/admin/'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешно завершена')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при регистрации')
    else:
        form = UserRegisterForm()    
    context = {
        'form': form
    }
    return render(request, 'blog/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserAuthForm()
    context = {
        'form': form
    }
    return render(request, 'blog/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')