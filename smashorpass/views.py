from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.http import HttpResponse
from smashorpass.models import *

    # Create your views here.
def suvrotronics(request):
    return render(request,"suvrotronics.html")
@login_required(login_url='login')
def home(request):
    return render(request,"home.html")
@login_required(login_url='login')
def post_list(request):
    post = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'post': post
    }
    return render(request, 'posts.html', context)
@login_required(login_url='login')
def post_detail(request,slug):
    postd = Post.objects.get(slug=slug)
    context = {
        'postd': postd
    }
    return render(request, 'post_detail.html', context)
@login_required(login_url='login')
def project_list(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    return render(request, 'projects.html', context)
@login_required(login_url='login')
def project1_detail(request):
    return render(request, 'project1_detail.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context={'form' :form}
    return render(request,"register.html",context)

def login(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth_login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Incorrect login info!')



               

    context={}
    return render(request,"login.html",context)
 
def logout(request):

    django_logout(request)
    return redirect('login')



