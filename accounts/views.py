from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from myapp.views import home
from .views import login
from myapp.views import home

def open(request):
    return render(request, 'accounts/open.html')
# Leads to open html webpage

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            # Save form to database
            form.save()

            # Retrieve username and password
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            user = authenticate(request, username=username, password=raw_password)

            # If registering is successful leads back to open webpage with new user
            if user is not None:
                login(request, user=user)
                return redirect('open')
            
            else:
                # If registering is unsuccessful stays on register page
                return render(request, 'accounts/register.html', {'form': form, 'error': 'Authentication failed'})
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        # Retrieves username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Checks login is succesful
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'accounts/login.html')

