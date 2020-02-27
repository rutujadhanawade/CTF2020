from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.models import User,auth


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
        user.save();
        userprofile.save();
        print("user succesfully created")

        return redirect('login')

    elif request.method == 'GET':
        return render(request, 'ctf/signup.html')

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request, 'invalid credentials')
                return redirect('ctf/login.html')
        else:
            return render(request, 'ctf/login.html')
