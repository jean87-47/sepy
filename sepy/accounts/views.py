from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import User
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

User=settings.AUTH_USER_MODEL



def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:list')
    if request.method == "POST" :
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('articles:index')
    else:
        form=CustomUserCreationForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)


def detail(request,pk):
    User=get_user_model()
    user=get_object_or_404(User,pk=pk)
    context={'user':user}
    return render(request,'accounts/detail.html',context)

def update(request,pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    if request.method== "POST":
        form=CustomUserChangeForm(request.POST,instance=user)
        if form.is_valid():
            user=form.save()
            user.save()
        return redirect('accounts:detail',pk=user.pk)
    else :
        form=CustomUserChangeForm(instance=user)
        context={'form':form}
    return render(request,'accounts/update.html',context)

def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form=AuthenticationForm()
        context={'form':form}
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_POST
@login_required
def delete(request) :
    request.user.delete()
    return redirect('articles:index')

def follow(request,pk):
    User=get_user_model()
    user=get_object_or_404(User,pk=pk)
    if user != request.user :
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('accounts:detail',pk=user.pk)


