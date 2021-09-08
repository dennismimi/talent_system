from django.shortcuts import redirect, render
from .form import *
from django.urls import reverse
from .models import *

def index(request):
    templates = 'dashboard.html'
    context = {}
    return render(request,templates,context)

def about(request):
    templates = 'about.html'
    context = {}
    return render(request,templates,context)

def registerTeam(request):
    if request.method == "GET":
        template = "Entry/teamReg.html"
        context = {"form": TeamRegisterForm}
        return render(request, template, context)
    
    elif request.method == "POST":
        form = TeamRegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            obj = Team()
            obj.name = form.cleaned_data['name']
            obj.location = form.cleaned_data['location']
            obj.coachName = form.cleaned_data['coachName']
            obj.playersNo = form.cleaned_data['playersNo']
            obj.winnings = form.cleaned_data['winnings']
            obj.losses = form.cleaned_data['losses']
            obj.draw = form.cleaned_data['draw']
            obj.save()
            return redirect(reverse("index"))
        else:
            template = "Entry/teamReg.html"
            context = {"form": TeamRegisterForm}
            return render(request, template, context)
        
def registerPlayer(request):
    if request.method == "GET":
        template = "Entry/teamReg.html"
        context = {"form": PlayerRegisterForm}
        return render(request, template, context)
    
    elif request.method == "POST":
        form = PlayerRegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            obj = Player()
            obj.name = form.cleaned_data['name']
            obj.team = form.cleaned_data['team']
            obj.nickname = form.cleaned_data['nickname']
            obj.role = form.cleaned_data['role']
            obj.location = form.cleaned_data['location']
            obj.age = form.cleaned_data['age']
            obj.playerImage = form.cleaned_data['playerImage']
            obj.save()
            return redirect(reverse("index"))
        else:
            template = "Entry/teamReg.html"
            context = {"form": PlayerRegisterForm}
            return render(request, template, context)

def commentTab(request):
    if request.method == "GET":
        template = "Entry/comment.html"
        context = {"form": CommentForm}
        return render(request, template, context)
    
    elif request.method == "POST":
        form = CommentForm(request.POST, request.FILES or None)
        if form.is_valid():
            obj = Comment()
            obj.title = form.cleaned_data['title']
            obj.comment = form.cleaned_data['comment']
            obj.date = form.cleaned_data['date']
            obj.save()
            return redirect(reverse("index"))
        else:
            template = "Entry/comment.html"
            context = {"form": CommentForm}
            return render(request, template, context)
        
def voteSection(request):
    if request.method == "GET":
        template = "Entry/teamReg.html"
        context = {"form": VoteForm}
        return render(request, template, context)
    
    elif request.method == "POST":
        form = VoteForm(request.POST, request.FILES or None)
        if form.is_valid():
            obj = Vote()
            obj.nickname = form.cleaned_data['nickname']
            obj.date = form.cleaned_data['date']
            obj.rating = form.cleaned_data['rating']
            obj.save()
            return redirect(reverse("index"))
        else:
            template = "Entry/teamReg.html"
            
            context = {"form": VoteForm}
            return render(request, template, context)
        
def reportMvp(request):
    voteResults = Vote.objects.all()
    templates = 'report.html'
    context = {'votes': voteResults}
    return render(request, templates, context)

def reportComments(request):
    commentResults = Comment.objects.all()
    templates = 'report.html'
    context = {'comments': commentResults}
    return render(request, templates, context)