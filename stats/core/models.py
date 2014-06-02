from django.db import models

# Create your models here.
class Player(models.Model):
	playerid = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Batter(models.Model):
	batterid = models.AutoField(primary_key=True)
	batter = models.ForeignKey(Player)
	season = models.IntegerField()
	battingavg = models.DecimalField(max_digits=4, decimal_places=3)

class Pitcher(models.Model):
	pitcherid = models.AutoField(primary_key=True)
	pitcher = models.ForeignKey(Player)
	season = models.IntegerField()
	era = models.DecimalField(max_digits=5, decimal_places=3)

class AtBat(models.Model):
	atbatid = models.AutoField(primary_key=True)
	batter = models.ForeignKey(Batter)
	pitcher = models.ForeignKey(Pitcher)
	game = models.ForeignKey(Game)

class Pitch(models.Model):
	pitchid = models.AutoField(primary_key=True)
	pitcher = models.ForeignKey(Pitcher)
	atbat = models.ForeignKey(AtBat)
	game = models.ForeignKey(Game)

class Game(models.Model):
	gameid = models.AutoField(primary_key=True)
	home =  models.CharField(max_length=30)
