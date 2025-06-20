from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# update
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# from .forms import  CustomUserChangeForm
# from django.contrib.auth.forms import  PasswordChangeForm



# Create your views here.
@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        redirect('movies:index')
    
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request, 'accounts/login.html',context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form=CustomUserCreationForm()
    context={
        'form':form
    }
    return render(request,'accounts/signup.html',context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context={
        'form':form
    }
    return render(request,'accounts/update.html', context)

@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form=PasswordChangeForm(request.user)
    context={
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)
