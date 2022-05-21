from django import template
from blog.models import Category
from django.db.models import Count, F
from django.core.cache import cache

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blog/include/list_categories.html')
def show_categories():
    # categories = Category.objects.all()  # Выводит весь список категорий

    categories = cache.get('categories')                                # Пытаемся получить данные из кэша
    if not categories:                                                  # Если в кэше данных нет...
        # Если категория пустая - ее не будет в списке категорий, 
        # в счетчике учитываются только опубликованные записи
        categories = Category.objects.annotate(notes=Count(             # ...получаем их из базы данных... 
            'blog', 
            filter=F('blog__is_published'))).filter(notes__gt=0)
        cache.set('categories', categories, 15)                         # ...и кладем в кэш, где они пробудут N секунд
    return {'categories': categories}