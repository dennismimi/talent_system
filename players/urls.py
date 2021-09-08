from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('teamRegister/', registerTeam, name="registerTeam"),
    path('playerRegister/', registerPlayer, name="playerRegister"),
    path('comments/', commentTab, name="comments"),
    path('vote/', voteSection, name="vote"),
    path('about/', about, name="about"),
    path('report/', reportMvp, name="report"),
    path('comment/', reportComments, name="comment"),
]
