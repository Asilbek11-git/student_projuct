from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, permission_required



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz. Tizimga kiring!")
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'accounts/register.html', {'form': form})





@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def home(request):
    return render(request,'home.html')



