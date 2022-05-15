from django import forms
from .models import Category, Blog
from django.forms import ModelForm, TextInput, Textarea, Select
import re
from django.core.exceptions import ValidationError

# Форма не связана с моделью

''' class BlogForm(forms.Form):
    
    title = forms.CharField(
        max_length=50, 
        label='Заголовок', 
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Заголовок'
        })
    )

    text = forms.CharField(
        label='Содержание', 
        required=False, 
        widget=forms.Textarea(attrs={
            'class': 'textarea',
            'placeholder': 'Содержание'
        })
    )

    is_published = forms.BooleanField(
        label='Опубликовать', 
        initial=True
    )


    category = forms.ModelChoiceField(
        empty_label='Выберите категорию', 
        queryset=Category.objects.all(), 
        label='Категория', 
        widget=forms.Select(attrs={
            'class': 'select'
        })
    )
 '''

# Форма связана с моделью

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'is_published', 'category']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Заголовок'
            }),
            'text': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Содержание'
            }),
            'category': forms.Select(attrs={
                'class': 'select'
            }),
        }

    # Валидатор title
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Заголовок не должен начинаться с цифры')
        return title

    # Валидатор text
    def clean_text(self):
        text = self.cleaned_data['text']
        if re.match(r'\d', text):
            raise ValidationError('Содержание записи не должно начинаться с цифры')
        return text