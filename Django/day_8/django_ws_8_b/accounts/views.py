from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
# from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.get_user)
            return redirect('todos:index')
        
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)