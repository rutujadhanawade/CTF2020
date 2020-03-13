from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('register', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('login', views.login1, name='login1'),
    path('instructions', views.inst, name='inst'),
    path('QUEST', views.Quest, name='Quest'),
    path('logout', views.logout, name='logout'),
    path('check', views.check, name='check'),
    path('hint', views.hint, name='hint'),
    path('leaderboard', views.leaderboard, name='leaderboard')
]
# def leaderboard(request):
#     #data = Submission.objects.all().order_by("-curr_score", "-sub_time")
#     sorteduser = UserProfile.objects.all().order_by("-score")
#     # count =4
#     # sub_list = []
#     # for element in sorteduser:
#     #     if count < 4:
#     #         sub = Submission.objects.get(user=element.user)
#     #         sub_list.append(sub)
#     #         print(sub_list)
#     #         count -= 1
#     #     else:
#     #         return render(request, 'ctf/hackerboard.html', context={'sub': sub_list, 'user': sorteduser})
