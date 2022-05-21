from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(BlogView.as_view()), name='home'),  # Сохранение главной страницы в кэшэ на 60 секунд
    path('category/<int:category_id>/', BlogCategory.as_view(), name='category'),
    path('notes/create/', BlogCreateView.as_view(), name='add_note'),
    path('notes/<int:pk>/', BlogDetailView.as_view(), name='view_note'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('feedback/', feedback, name='feedback'),
]