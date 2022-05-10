from django.contrib import admin
from .models import Blog
# Зарегистрируйте свои модели здесь.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_ad', 'updated_ad', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')

admin.site.register(Blog, BlogAdmin)
