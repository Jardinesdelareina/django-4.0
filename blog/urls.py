from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('category/<int:category_id>/', BlogCategory.as_view(), name='category'),
    path('notes/<int:pk>/', BlogDetailView.as_view(), name='view_note'),
    path('notes/add_note/', add_note, name='add_note'),
]