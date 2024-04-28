from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    # Homepage
    path('fetch_subreddit/', views.fetch_subreddit_view, name='fetch_subreddit')
]
    