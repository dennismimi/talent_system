from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    coachName = models.CharField(max_length=30)
    playersNo = models.IntegerField(default=11)
    winnings = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    age = models.IntegerField()
    playerImage = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    title = models.CharField(max_length=30)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Vote(models.Model):
    nickname = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(max_length=100)

    def __str__(self):
        return self.nickname.name