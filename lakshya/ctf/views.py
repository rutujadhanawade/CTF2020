from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile, Questions, Submission
from django.contrib.auth.models import User, auth


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
        score = 0
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'ctf/signup.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username= request.POST['username'],password= request.POST['password'])
                userprofile = UserProfile(user=user, email=email, phone=phone, clg=clg, dept=dept, firstname=firstname, lastname=lastname, year=year, score=score)
                userprofile.save()
        # login(request, user)
                return render(request, 'ctf/first.html', context={'user': user})
        else:
            return render(request, 'ctf/signup.html', {'error': "Password doesnt match"})

    elif request.method == 'GET':
        return render(request, 'ctf/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('ctf/first.html')
        else:
            messages.error(request, 'Invalid credentials!')

    return render(request, 'ctf/login.html')


def first(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    questions = Questions.objects.all().order_by('Qid')
    if (request.method == 'POST'):
        req = request.POST
        Qid = req.get('Qid')
        flag = req.get('flag')
        quest = Questions.objects.get(Qid=int(Qid))
        quest.Qid = Qid
        print("in views")
        print(str(request.user))
        print(request.user.username)
        solved = Submission.objects.filter(question=quest,user=userprofile)
        #print("Third" + str(quest.Qid))
        #print(str(quest.Qid) + ":" + quest.flag)
        #print(flag)
        if (flag == quest.flag):
            if not solved:
                solved = Submission()
                userprofile.score += quest.points
                solved.question = quest
                solved.user = userprofile
                quest.solved += 1
                userprofile.save()
                solved.save()

                print(userprofile.score)
                print("FLAG IS CORRECT!")
                messages.success(request, 'FLAG IS CORRECT!')
            else:
                messages.warning(request, 'ALREADY SOLVED!')
        else:
            print("INCORRECT")
            messages.success(request, 'FLAG IS WRONG!')
        userprofile.save()
        quest.save()
    return render(request, 'ctf/first.html', {'questions':questions, 'userprofile':userprofile})

def logout(request):
    auth.logout(request)
    return redirect("/")

