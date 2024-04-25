from django.shortcuts import render, redirect
from .processing_data.reddit_api import fetch_subreddit
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


@login_required
def home(request):
    return render(request, 'myapp/home.html', {'first_name': request.user.first_name})
        # if request.user.
    # return render(request, 'myapp/home.html')

def fetch_subreddit_view(request):
    if request.method == "POST":
        positive_summary, negative_summary = fetch_subreddit(request)
        return render(request, 'myapp/results.html', {
            'positive': positive_summary, 
            'negative': negative_summary
        })
    else:
        return render(request, 'home.html')


# def my_view(request):
#     user = request.user
#     return render(request, 'home.html', {'first_name': user.first_name})