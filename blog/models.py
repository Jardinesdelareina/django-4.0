from django.urls import reverse
from django.db import models

# Создавайте свои модели здесь.

class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Содержание', max_length=2000)
    created_ad = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_ad = models.DateTimeField('Обновлено', auto_now=True)
    image = models.ImageField('Изображение', upload_to='image/%Y/%m/%d', blank=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=1)

    def get_absolute_url(self):
        return reverse('view_note', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_ad']


class Category(models.Model):
    title = models.CharField('Наименование категории', max_length=50, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
