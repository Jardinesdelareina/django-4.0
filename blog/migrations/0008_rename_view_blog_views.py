# Generated by Django 4.0.4 on 2022-05-16 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_view_alter_blog_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='view',
            new_name='views',
        ),
    ]
