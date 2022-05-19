from django import template
from blog.models import Category
from django.db.models import Count, F

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blog/include/list_categories.html')
def show_categories():
    # categories = Category.objects.all()  # Выводит весь список категорий

    # Если категория пустая, она отсутствует в списке категорий, в счетчике учитываются только опубликованные записи
    categories = Category.objects.annotate(notes=Count('blog', filter=F('blog__is_published'))).filter(notes__gt=0)
    return {'categories': categories}