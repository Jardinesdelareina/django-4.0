from django.db import models

# Создавайте свои модели здесь.

class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Содержание', max_length=2000)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title