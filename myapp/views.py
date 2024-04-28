from django.shortcuts import render
from .processing_data.reddit_api import fetch_subreddit
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'myapp/home.html', {'first_name': request.user.first_name})
# Successufl login leads to the front page and the first name is stored

def fetch_subreddit_view(request):
    if request.method == "POST":
        positive_summary, negative_summary = fetch_subreddit(request)
        return render(request, 'myapp/results.html', {
            'positive': positive_summary, 
            'negative': negative_summary
        })
    # Goes to results page with positive summary and negative summary
    else:
        return render(request, 'home.html')
    
    
