# Generated by Django 4.0.4 on 2022-05-15 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at'], 'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='updated_ad',
            new_name='updated_at',
        ),
    ]