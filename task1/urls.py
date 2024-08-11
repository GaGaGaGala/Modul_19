from django.urls import path
from . import views
urlpatterns = [
    path('cart/', views.get_cart, name='get_cart'),
    path('games/', views.get_games, name='get_games'),
    path('platform/', views.get_cart, name='get_platform'),
    path('menu/', views.get_cart, name='get_menu'),
    path('sign_up_html/', views.sign_up_by_html, name='sign_up_by_html'),
    path('sign_up_django/', views.sign_up_by_django, name='sing_up_by_django'),
]