from django import forms
from datetime import date
from .models import Team,Player
class TeamRegisterForm(forms.Form):
    name = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    coachName = forms.CharField(max_length=30)
    playersNo = forms.IntegerField()
    winnings = forms.IntegerField()
    losses = forms.IntegerField()
    draw = forms.IntegerField()


class PlayerRegisterForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(),)
    name = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=30)
    role = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    age = forms.IntegerField()
    playerImage = forms.ImageField()


class CommentForm(forms.Form):
    title = forms.CharField(max_length=30)
    comment = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField(initial =date.today)


class VoteForm(forms.Form):
    nickname = forms.ModelChoiceField(queryset=Player.objects.all())
    date = forms.DateTimeField(initial =date.today)
    rating = forms.IntegerField()
