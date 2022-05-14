from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('notes/<int:note_id>/', get_note, name='view_note'),
    path('notes/add_note/', add_note, name='add_note'),
]