from django.db import models

# Create your models here.
class Player(models.Model):

	player_id = models.AutoField(primary_key=True)

	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	
	given_name = models.CharField(max_length=60)

	weight = models.IntegerField()
	height = models.IntegerField()

	bats = models.CharField(max_length=3)
	throws = models.CharField(max_length=3)
	debut_game = models.DateField(null=True)
	final_game = models.DateField(null=True)

	mlb_id = models.CharField(max_length=12)
	retro_id = models.CharField(max_length=12)
	bbref_id = models.CharField(max_length=12)
	lahman_id = models.CharField(max_length=12, unique=True)

	birth_year = models.IntegerField()
	birth_month = models.IntegerField()
	birth_day = models.IntegerField()
	birth_country = models.CharField(max_length=30)
	birth_state = models.CharField(max_length=30)
	birth_city = models.CharField(max_length=30)

	death_year = models.IntegerField(null=True)
	death_month = models.IntegerField(null=True)
	death_day = models.IntegerField(null=True)
	death_country = models.CharField(max_length=30, null=True)
	death_state = models.CharField(max_length=30, null=True)
	death_city = models.CharField(max_length=30, null=True)


class BatterSeason(models.Model):
	batter_season_id = models.AutoField(primary_key=True)
	player_id = models.ForeignKey(Player, db_column='lahman_id')
	season = models.IntegerField()
	team = models.ForeignKey(FranchiseTeam, db_column='lahman_id')
	games = models.IntegerField()
	plate_appearances = models.IntegerField()
	at_bats = models.IntegerField()
	runs = models.IntegerField()
	hits = models.IntegerField()
	doubles = models.IntegerField()
	triples = models.IntegerField()
	home_runs = models.IntegerField()

	@property
	def singles(self):
		return self.hits - self.double - self.triple - self.home_runs
	# singles = property(_get_singles)
	
	rbis = models.IntegerField()
	stolen_bases = models.IntegerField()

	caught_stealing = models.IntegerField()

	walks = models.IntegerField()
	strike_outs = models.IntegerField()
	battingavg = models.DecimalField(max_digits=4, decimal_places=3)
	obp = models.DecimalField(max_digits=4, decimal_places=3)

	@property
	def slg(self):
		return (self.singles + 2*self.doubles + 3*self.triples + 4*self.home_runs)/self.at_bats
	# slg = property(_get_slg)
	
	@property
	def ops(self):
		return self.obp + self.slg
	# ops = property(_get_ops)

	salary = models.IntegerField()

	# stolen_bases_2 = models.IntegerField()
	# stolen_bases_3 = models.IntegerField()
	# stolen_bases_4 = models.IntegerField()
	# caught_stealing_2 = models.IntegerField()
	# caught_stealing_3 = models.IntegerField()
	# caught_stealing_4 = models.IntegerField()
	# pickoffs = models.IntegerField()
	# caught_stealing_pickoffs = models.IntegerField()
	# oob = models.IntegerField()
	# oob1 = models.IntegerField()
	# oob2 = models.IntegerField()
	# oob3 = models.IntegerField()
	# oob4 = models.IntegerField()
	# first_single = models.IntegerField()
	# first_single_second = models.IntegerField()
	# first_single_third_home = models.IntegerField()
	# first_double = models.IntegerField()
	# first_double_third = models.IntegerField()
	# first_double_home = models.IntegerField()
	# second_single = models.IntegerField()
	# second_single_third = models.IntegerField()
	# second_single_home = models.IntegerField()
	# bases_taken = models.IntegerField()
	# ops_plus = models.IntegerField()
	# total_bases = models.IntegerField()
	# gdp = models.IntegerField()
	# hbp = models.IntegerField()
	# sac_hits = models.IntegerField()
	# sac_flys = models.IntegerField()
	# ibb = models.IntegerField()
	# runs_batting = models.IntegerField()
	# runs_basing = models.IntegerField()
	# rdp = models.IntegerField()
	# runs_fielding = models.IntegerField()
	# rpos = models.IntegerField()
	# raa = models.IntegerField()
	# waa = models.DecimalField(max_digits=2, decimal_places=1)
	# rrep = models.IntegerField()
	# rar = models.IntegerField()
	# war = models.DecimalField(max_digits=2, decimal_places=1)
	# waawl = models.DecimalField(max_digits=4, decimal_places=3)
	# seasonwl = models.DecimalField(max_digits=4, decimal_places=3)
	# owar = models.DecimalField(max_digits=2, decimal_places=1)
	# dwar = models.DecimalField(max_digits=2, decimal_places=1)
	# orar = models.DecimalField(max_digits=2, decimal_places=1)

class Franchise(models.Model):
	franchise_id = models.CharField(primary_key=True, max_length=3)
	franchise_name = models.CharField(max_length=40)
	active = models.CharField(max_length=3)
	national_association = models.CharField(max_length=3)

class FranchiseTeam(models.Model):
	franchise_id = models.ForeignKey(Franchise)
	lahman_id = models.CharField(max_length=3, unique=True)

class Team(models.Model):
	team_id = models.AutoField(primary_key=True)
	franchise_id = models.ForeignKey(Franchise)
	to_unique_id = models.ForeignKey(FranchiseTeam, db_column="team_id")
	retro_id = models.CharField(max_length=5)
	lahman_id = models.CharField(max_length=5)

	lg_id = models.CharField(max_length=3)
	dv_id = models.CharField(max_length=3)

	team_city = models.CharField(max_length=20)
	team_name = models.CharField(max_length=20)
	team_nickname = models.CharField(max_length=20)

	first_year = models.DateField()
	last_year = models.DateField(null=True)

	loc_city = models.CharField(max_length=20)
	loc_state = models.CharField(max_length=20)

class TeamSeason(models.Model):
	to_unique_id = models.ForeignKey(Franchise, db_column="team_id")
	year = models.IntegerField()
	games = models.IntegerField()
	wins = models.IntegerField()
	losses = models.IntegerField()

	rank = models.IntegerField()
	div_win = models.BooleanField()
	wc_win = models.BooleanField()
	lg_win = models.BooleanField()
	ws_win = models.BooleanField()

	runs = models.IntegerField()
	at_bats = models.IntegerField()
	hits = models.IntegerField()
	doubles = models.IntegerField()
	triples = models.IntegerField()
	home_runs = models.IntegerField()
	walks = models.IntegerField()
	strike_outs = models.IntegerField()
	stolen_bases = models.IntegerField()
	caught_stealing = models.IntegerField()
	hbp = models.IntegerField()
	sac_flys = models.IntegerField()
	ra = models.IntegerField()
	
	earned_runs = models.IntegerField()
	era = models.DecimalField(max_digits=4, decimal_places=2)
	complete_games = models.IntegerField()
	shutouts = models.IntegerField()
	saves = models.IntegerField()
	outs_pitched = models.IntegerField()
	hits_allowed = models.IntegerField()
	home_runs_allowed = models.IntegerField()
	walks_allowed = models.IntegerField()
	strike_out_pitching = models.IntegerField()

	errors = models.IntegerField()
	double_plays = models.IntegerField()
	fielding_percentage = models.DecimalField(max_digits=3, decimal_places=3)

	park = models.CharField(max_length=40)
	attendance = models.IntegerField()
	bpf = models.IntegerField()
	ppf = models.IntegerField()





# class Pitcher(models.Model):
# 	pitcherid = models.AutoField(primary_key=True)
# 	pitcher = models.ForeignKey(Player)
# 	season = models.IntegerField()
# 	era = models.DecimalField(max_digits=5, decimal_places=3)

# class AtBat(models.Model):
# 	atbatid = models.AutoField(primary_key=True)
# 	batter = models.ForeignKey(Batter)
# 	pitcher = models.ForeignKey(Pitcher)
# 	game = models.ForeignKey(Game)

# class Pitch(models.Model):
# 	pitchid = models.AutoField(primary_key=True)
# 	pitcher = models.ForeignKey(Pitcher)
# 	atbat = models.ForeignKey(AtBat)
# 	game = models.ForeignKey(Game)

# class Game(models.Model):
# 	gameid = models.AutoField(primary_key=True)
# 	home =  models.CharField(max_length=30)

