from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('category/<int:category_id>/', BlogCategory.as_view(), name='category'),
    path('notes/create/', BlogCreateView.as_view(), name='add_note'),
    path('notes/<int:pk>/', BlogDetailView.as_view(), name='view_note'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]