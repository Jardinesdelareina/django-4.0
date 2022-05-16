from django.contrib import admin
from .models import Blog, Category
# Зарегистрируйте свои модели здесь.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'text')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
