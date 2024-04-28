from django.urls import path, include
from . import views

urlpatterns = [
    path('open/', views.open, name='open'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
    