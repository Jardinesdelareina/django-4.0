from django import template
from blog.models import Category
from django.db.models import Count

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blog/include/list_categories.html')
def show_categories():
    # categories = Category.objects.all()  # Выводит весь список категорий
    categories = Category.objects.annotate(notes=Count('blog')).filter(notes__gt=0)  # Если категория пустая, она отсутствует в списке категорий
    return {'categories': categories}