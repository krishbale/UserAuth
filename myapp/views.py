from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def index(request):
    features = Feature.objects.all()
   
  
    return render (request, 'index.html',{'features':features})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
    
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password Not the Same')
            return redirect('register')    
    return render(request , 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/') 
        else:
            messages.info(request,"credentials Invalid")
            return redirect('login')
    


    
    return render(request,'login.html') 
def logout(request):
    auth.logout(request)
    return redirect('/')
def post(request,pk):
    return render(request,'post.html',{'pk':pk})
    
  