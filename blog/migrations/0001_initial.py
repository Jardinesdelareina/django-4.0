# Generated by Django 4.0.4 on 2022-05-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=2000, verbose_name='Содержание')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
