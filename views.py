from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages,auth
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.models import User


def index(request):
    return render(request, 'ctf/HOME.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'ctf/HOME.html')
        else:
            messages.error(request, 'Invalid credentials!')

    return render(request, 'ctf/login.html')

def signup(request):
    if request.method == "POST":
        # to create a user
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        clg = request.POST.get('clg')
        dept = request.POST.get('dept')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        year = request.POST.get('year')
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'ctf/signup.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username= request.POST['username'],password= request.POST['password'])
                userprofile = UserProfile(user=user, email=email, phone=phone, clg=clg, dept=dept, firstname=firstname,
                                           lastname=lastname, year=year)
                auth.login(request, user)
                return render(request, 'ctf/login.html')
        else:
            return render(request, 'ctf/signup.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'ctf/signup.html')