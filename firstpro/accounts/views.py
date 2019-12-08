from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):
    
    if request.method == 'POST' :
        First_name = request.POST["FIRST NAME"]
        Last_name = request.POST["LAST NAME"]
        User_name = request.POST["User Name"]
        Email = request.POST["EMAIL"]
        Password1 = request.POST["Password"]
        Password2 = request.POST["Confirm Password"]
        if Password1 == Password2:
            if User.objects.filter(username = User_name).exists():
                #print("user already exists")
                messages.info(request, "user already exists")
                return render(request, 'register.html')
            elif User.objects.filter(email = Email).exists():
                #print("email already exists")
                messages.info(request, "email already exists")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(first_name=First_name, last_name=Last_name, username=User_name,email=Email,password=Password1)
                user.save();
                messages.info(request, "user created")
                return render(request, 'register.html')     
        else:
           messages.info(request, "Password Not Matching")
           return render(request, 'register.html')
        return redirect('/')        
    else:
        return render(request,'register.html')
    