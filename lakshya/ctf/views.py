from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse
import datetime
import time
from .models import UserProfile, Questions, Submission
from django.contrib.auth.models import User, auth

endtime = 0
duration = 2700


def index(request):
    return render(request, 'ctf/index.html')


def error(request):
    return render(request, 'ctf/404.html')


def about(request):
    return render(request, 'ctf/about.html')


def inst(request):
    return render(request, 'ctf/instructions.html')


def hint(request):
    if request.method == 'POST':
        question = Questions.objects.get(Qid=request.POST.get('id'))
        hint = question.Hint
        questionPoints = question.points
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user=user)
        try:
            solved = Submission.objects.filter(question=question, user=userprofile)
            return HttpResponse(hint)
        except Submission.DoesNotExist:
            solved = Submission()
            userprofile.score -= questionPoints * 0.1
            solved.question = question
            solved.user = userprofile
            solved.curr_score = userprofile.score
            solved.save()
            userprofile.save()
            return HttpResponse(hint)
    return render(request, 'ctf/404.html')


def check(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    questions = Questions.objects.all().order_by('Qid')
    if request.method == 'POST':
        req = request.POST
        Qid = req.get('Qid')
        flag = req.get('flag')
        level = req.get('customRadio')
        quest = Questions.objects.get(Qid=int(Qid))
        quest.Qid = Qid
        if level == None:
            return HttpResponse("-1")
        else:
            quest.level = level
            quest.save()

            solved = Submission.objects.filter(question=quest, user=userprofile)

            if flag == quest.flag:
                if not solved:
                    solved = Submission()
                    userprofile.score += quest.points
                    solved.question = quest
                    solved.user = userprofile
                    solved.curr_score = userprofile.score

                    sec = calc()
                    sec = duration-sec
                    solved.sub_time = time.strftime("%H:%M:%S", time.gmtime(sec))
                    userprofile.latest_sub_time = solved.sub_time
                   # solved.sub_time = '{}:{}:{}'.format(hour, min, sec)
                    print(solved.sub_time)
                    quest.solved += 1
                    solved.solved = 1
                    userprofile.totlesub += 1
                    userprofile.save()
                    solved.save()

                    print(userprofile.score)
                    print("FLAG IS CORRECT!")
                    return HttpResponse('1')

                else:
                    return HttpResponse('2')
            else:
                print("INCORRECT")
                return HttpResponse('0')
            userprofile.save()
            quest.save()
    return HttpResponse("")


def timer():
    start = datetime.datetime.now()
    starttime = start.hour * 60 * 60 + start.minute * 60 + start.second
    global duration
    global endtime
    endtime = starttime + int(duration)
    print(starttime)
    return start


def calc():
    global endtime
    now = datetime.datetime.now()
    nowsec = now.hour * 60 * 60 + now.minute * 60 + now.second
    diff = endtime - nowsec
    print(diff)
    if nowsec <= endtime:
        return diff
    else:
        return 0


def signup(request):
    if request.method == 'POST':
        recid = request.POST.get('reciept_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        score = 0

        try:
            user = User.objects.get(username=username)
            return render(request, 'ctf/register.html', {'error': "Username Has Already Been Taken"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            # time = timer()
            userprofile = UserProfile(user=user, Rid=recid, score=score)
            userprofile.save()
            timer()
            login(request, user)

            return redirect("inst")

    elif request.method == 'GET':
        return render(request, 'ctf/register.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            userprofile = UserProfile.objects.get(user=user)
            userprofile.time = timer()
            userprofile.save()
            return redirect("inst")
        else:
            messages.error(request, 'Invalid credentials!')

    return render(request, 'ctf/login.html')


def Quest(request):
    var = calc()
    if var != 0:
        user = User.objects.get(username=request.user.username)
        userprofile = UserProfile.objects.get(user=user)
        questions = Questions.objects.all().order_by('Qid')
        submission = Submission.objects.filter(user=userprofile)
        submission_q_id = Submission.objects.values_list('question_id', flat=True).filter(user=userprofile)
        # if request.method == 'POST':
        #     req = request.POST
        #     Qid = req.get('Qid')
        #     flag = req.get('flag')
        #     level = req.get('customRadio')
        #     print(level)
        #     quest = Questions.objects.get(Qid=int(Qid))
        #     quest.Qid = Qid
        #     quest.level = level
        #     quest.save()
        #     print("in views")
        #     print(str(request.user))
        #     print(request.user.username)
        #     solved = Submission.objects.filter(question=quest, user=userprofile)
        #
        #     if flag == quest.flag:
        #         if not solved:
        #             solved = Submission()
        #             userprofile.score += quest.points
        #             solved.question = quest
        #             solved.user = userprofile
        #             time = calc()
        #           #  solved.sub_time = tim
        #           #  user.time = solved.sub_time
        #             quest.solved += 1
        #             userprofile.totlesub += 1
        #             userprofile.save()
        #             solved.save()
        #
        #
        #             print(userprofile.score)
        #             print("FLAG IS CORRECT!")
        #             messages.success(request, 'FLAG IS CORRECT!')
        #         else:
        #             messages.warning(request, 'ALREADY SOLVED!')
        #     else:
        #         print("INCORRECT")
        #         messages.success(request, 'FLAG IS WRONG!')
        #     userprofile.save()
        #     quest.save()
        return render(request, 'ctf/quests.html',
                      {'questions': questions, 'userprofile': userprofile, 'time': var, 'submission': submission,
                       'submission_q_id': submission_q_id})
    else:
        return HttpResponse("time is 0:0")


def logout(request):
    auth.logout(request)
    return redirect("/")


def leaderboard(request):
    #data = Submission.objects.all().order_by("-curr_score", "-sub_time")
    user = UserProfile.objects.all().order_by("-score")

    sub = Submission.objects.all().filter(user=user)[:4]
    return render(request, 'ctf/hackerboard.html', context={'sub': sub, 'user': user})


'''''def first(request):
    var = calc()
    if var != 0:
        return render(request, 'ctf/first.html', context={'time': var})
    else:
        return HttpResponse("time is 0:0")'''
