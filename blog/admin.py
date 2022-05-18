from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe

# Зарегистрируйте свои модели здесь.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'is_published', 'get_image', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'text')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        else:
            return '*'

    get_image.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Блог fueros'
admin.site.site_header = 'Управление записями'