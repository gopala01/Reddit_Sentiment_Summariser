from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    # Fields for first name, last name and email to ensure they are required
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        # Meta configures model and fields for the form
        model = User
        # Using Djangos built in User model
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


        