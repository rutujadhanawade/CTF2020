from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.models import User


def index(request):
    return render(request, 'ctf/HOME.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        clg = request.POST.get('clg')
        dept = request.POST.get('dept')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        year = request.POST.get('year')
        


        user = User.objects.create_user(username=username, password=password)
        userprofile = UserProfile(user=user, email=email, phone=phone, clg=clg, dept=dept, firstname=firstname,
                                  lastname=lastname, year=year)
        userprofile.save()
        login(request, user)

        return render(request, 'ctf/challenges.html', context={'user': user})

    elif request.method == 'GET':
        return render(request, 'ctf/signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'ctf/challenges.html')
        else:
            messages.error(request, 'Invalid credentials!')

    return render(request, 'ctf/login.html')

def userID(request):
    current_user = request.user
    if request.user.is_authenticated:
        current_user = request.user
    else:
        current_user = "Anonymous"

def logout1(request):
    print("into logout")
    logout(request)
    return render(request, 'ctf/HOME.html')

def challenges(request):
    if request.user.is_authenticated:
        return render (request, 'ctf/challenges.html')
    else:
        return redirect('login1')
