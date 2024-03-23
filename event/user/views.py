from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Userdetails
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def loginn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            error_message = "invalid username or password"
            return render(request, 'registration/login.html', {'error_message': error_message})
    return render(request,'registration/login.html')

def signup(request):
    if request.method=='POST':
        ad=request.POST['address']
        phone=request.POST['phone']
        email=request.POST['email']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['confirm_password']
        
        if password != password1:
            error_message = "Passwords do not match."
            return render(request, 'registration/signup.html', {'error_message': error_message})
        
        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            error_message = "This email is already registered."
            return render(request, 'registration/signup.html', {'error_message': error_message})
        
        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            error_message = "This username is already taken."
            return render(request, 'registration/signup.html', {'error_message': error_message})
        
        user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password)
        Userdetails.objects.create(user=user, address=ad, phone=phone)
        return redirect('login')
    return render(request,'registration/signup.html')

def logoutt(request):
    logout(request)
    return redirect('index')