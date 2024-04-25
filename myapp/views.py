from django.shortcuts import render, redirect
from .processing_data.reddit_api import fetch_subreddit
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'myapp/home.html')

def fetch_subreddit_view(request):
    if request.method == "POST":
        positive_summary, negative_summary = fetch_subreddit(request)
        return render(request, 'myapp/results.html', {
            'positive': positive_summary, 
            'negative': negative_summary
        })
    else:
        return render(request, 'home.html')
    

