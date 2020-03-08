from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse
import datetime
from .models import UserProfile
from django.contrib.auth.models import User, auth

endtime = 0


def index(request):
    return render(request, 'ctf/HOME.html')


def timer():
    start = datetime.datetime.now()
    starttime = start.hour*60*60 + start.minute*60 + start.second
    duration = 7200
    global endtime
    endtime = starttime + int(duration)
    print(starttime)
    return start


def calc():
    global endtime
    now = datetime.datetime.now()
    nowsec = now.hour * 60 * 60 + now.minute * 60 + now.second
    print(endtime)
    print(nowsec)
    diff = endtime - nowsec
    print(diff)
    if nowsec <= endtime:
        return diff
    else:
        return 0


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
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'ctf/signup.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                #time = timer()
                userprofile = UserProfile(user=user, email=email, phone=phone, clg=clg, dept=dept, firstname=firstname,
                                          lastname=lastname, year=year)
                userprofile.save()
                # login(request, user)
                timer()
                var = calc()
                return render(request, 'ctf/first.html', context={'user': user, 'time': var})
        else:
            return render(request, 'ctf/signup.html', {'error': "PAssword doesnt match"})

    elif request.method == 'GET':
        return render(request, 'ctf/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            timer()
            return redirect("first")
        else:
            messages.error(request, 'Invalid credentials!')

    return render(request, 'ctf/login.html')


def first(request):
    var = calc()
    if var != 0:
        return render(request, 'ctf/first.html', context={'time': var})
    else:
        return HttpResponse("time is 0:0")


def logout(request):
    auth.logout(request)
    return redirect("/")
