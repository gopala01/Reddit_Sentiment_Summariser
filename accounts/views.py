from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from myapp.views import home
from .views import login
from myapp.views import home

def open(request):
    return render(request, 'accounts/open.html')

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=email, password=raw_password)
            if user is not None:
                login(request, user=username)
                # return redirect('accounts/login.html')
                return redirect('open')
            else:
                return render(request, 'accounts/register.html', {'form': form, 'error': 'Authentication failed'})
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'accounts/login.html')

