from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Username")
    first_name = forms.CharField(required=True, label="First name")
    last_name = forms.CharField(required=True, label="Last name")
    phone_number = forms.CharField(required=True, label="Phone number")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number')



    
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email manzilingizni kiriting'
    }), label="Email")
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Parolingizni kiriting'
    }), label="Parol")