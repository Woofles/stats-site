from django.db import models

# Create your models here.
class Franchise(models.Model):
	franchise_id = models.CharField(primary_key=True, max_length=3)
	franchise_name = models.CharField(max_length=40)
	active = models.CharField(max_length=3)
	national_association = models.CharField(max_length=3)

class FranchiseTeam(models.Model):
	franchise_id = models.ForeignKey(Franchise)
	lahman_fid = models.CharField(max_length=3, unique=True)
	retro_id = models.CharField(max_length=5)

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
	lahman_pid = models.CharField(max_length=12, unique=True)

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

class Award(models.Model):
	player_id = models.ForeignKey(Player, to_field='lahman_pid')
	award_id = models.CharField(max_length=30)
	season = models.IntegerField()
	lg_id = models.CharField(max_length=2)
	tie = models.BooleanField()
	position = = models.CharField(max_length=3)

class BatterSeason(models.Model):
	#info
	batter_season_id = models.AutoField(primary_key=True)
	player_id = models.ForeignKey(Player, to_field='lahman_pid')
	season = models.IntegerField()
	team = models.ForeignKey(FranchiseTeam, to_field='lahman_fid')

	#basic
	games = models.IntegerField()
	games_batting = models.IntegerField()
	plate_appearances = models.IntegerField()
	at_bats = models.IntegerField()

	#plate
	runs = models.IntegerField()
	hits = models.IntegerField()
	singles = models.IntegerField()
	doubles = models.IntegerField()
	triples = models.IntegerField()
	home_runs = models.IntegerField()
	walks = models.IntegerField()
	rbis = models.IntegerField()
	strike_outs = models.IntegerField()
	sac_hits = models.IntegerField()
	sac_flys = models.IntegerField()
	gdp = models.IntegerField()
	hbp = models.IntegerField()
	ibb = models.IntegerField()
	total_bases = models.IntegerField()

	#running
	stolen_bases = models.IntegerField()
	stolen_bases_2 = models.IntegerField()
	stolen_bases_3 = models.IntegerField()
	stolen_bases_4 = models.IntegerField()
	caught_stealing = models.IntegerField()
	caught_stealing_2 = models.IntegerField()
	caught_stealing_3 = models.IntegerField()
	caught_stealing_4 = models.IntegerField()
	pickoffs = models.IntegerField()
	caught_stealing_pickoffs = models.IntegerField()
	oob = models.IntegerField()
	oob1 = models.IntegerField()
	oob2 = models.IntegerField()
	oob3 = models.IntegerField()
	oob4 = models.IntegerField()
	first_single = models.IntegerField()
	first_single_second = models.IntegerField()
	first_single_third_home = models.IntegerField()
	first_double = models.IntegerField()
	first_double_third = models.IntegerField()
	first_double_home = models.IntegerField()
	second_single = models.IntegerField()
	second_single_third = models.IntegerField()
	second_single_home = models.IntegerField()
	bases_taken = models.IntegerField()

	#stats
	battingavg = models.DecimalField(max_digits=4, decimal_places=3)
	obp = models.DecimalField(max_digits=4, decimal_places=3)
	slg = models.DecimalField(max_digits=4, decimal_places=3)
	ops = models.DecimalField(max_digits=4, decimal_places=3)
	ops_plus = models.IntegerField()

	#WAR...and such
	war = models.DecimalField(max_digits=2, decimal_places=1)
	owar = models.DecimalField(max_digits=2, decimal_places=1)
	dwar = models.DecimalField(max_digits=2, decimal_places=1)
	rar = models.IntegerField()
	runs_batting = models.IntegerField()
	runs_basing = models.IntegerField()
	rdp = models.IntegerField()
	runs_fielding = models.IntegerField()
	rpos = models.IntegerField()
	raa = models.IntegerField()
	waa = models.DecimalField(max_digits=2, decimal_places=1)
	rrep = models.IntegerField()
	waawl = models.DecimalField(max_digits=4, decimal_places=3)
	seasonwl = models.DecimalField(max_digits=4, decimal_places=3)
	orar = models.DecimalField(max_digits=2, decimal_places=1)

	#$$$$$$$
	salary = models.IntegerField()

class PitcherSeason(models.Model):
 	pitcher_id = models.AutoField(primary_key=True)
	player_id = models.ForeignKey(Player, to_field='lahman_pid')
	season = models.IntegerField()
	team = models.ForeignKey(FranchiseTeam, to_field='lahman_fid')

	#basic
	wins = models.IntegerField()
	losses = models.IntegerField()
	games = models.IntegerField()
	innings_pitched = models.DecimalField(max_digits=6, decimal_places=1)
	era = models.DecimalField(max_digits=5, decimal_places=3)

	#types
	saves = models.IntegerField()
	games_started = models.IntegerField()
	games_finished = models.IntegerField()
	complete_games = models.IntegerField()
	shutouts = models.IntegerField()

	#batting
	hits = models.IntegerField()
	runs = models.IntegerField()
	earned_runs = models.IntegerField()
	home_runs = models.IntegerField()
	walks = models.IntegerField()
	ibb = models.IntegerField()
	strike_outs = models.IntegerField()
	hbp = models.IntegerField()
	balks = models.IntegerField()
	wild_pitches = models.IntegerField()
	batters_faced = models.IntegerField()

	#more
	era_plus = models.IntegerField()
	fip = models.DecimalField(max_digits=4, decimal_places=2)
	whip = models.DecimalField(max_digits=5, decimal_places=3)
	hits_nine = models.DecimalField(max_digits=4, decimal_places=2)5
	home_runs_nine = models.DecimalField(max_digits=4, decimal_places=2)
	walks_nine = models.DecimalField(max_digits=4, decimal_places=2)
	strike_outs_nine = models.DecimalField(max_digits=5, decimal_places=2)
	strike_outs_walks = models.DecimalField(max_digits=4, decimal_places=2)

	ra9 = models.DecimalField(max_digits=4, decimal_places=2)
	ra9opp = models.DecimalField(max_digits=4, decimal_places=2)
	ra9def = models.DecimalField(max_digits=4, decimal_places=2)
	ra9role = models.DecimalField(max_digits=4, decimal_places=2)
	ppfp = models.DecimalField(max_digits=5, decimal_places=2)
	ra9avg = models.DecimalField(max_digits=4, decimal_places=2)
	raa = models.IntegerField()
	waa = models.DecimalField(max_digits=4, decimal_places=2)
	gm_li = models.DecimalField(max_digits=4, decimal_places=2)
	waaadj = models.DecimalField(max_digits=4, decimal_places=2)
	war = models.DecimalField(max_digits=4, decimal_places=2)
	rar = models.IntegerField()
	waawl= models.DecimalField(max_digits=4, decimal_places=3)
	seasonwl = models.DecimalField(max_digits=4, decimal_places=3)

	#$$$$$$
	salary = models.IntegerField()

class Team(models.Model):
	team_id = models.AutoField(primary_key=True)
	franchise_id = models.ForeignKey(Franchise)
	to_unique_id = models.ForeignKey(FranchiseTeam, to_field="lahman_fid")
	retro_id = models.CharField(max_length=5)
	lahman_tid = models.CharField(max_length=5)

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
	to_unique_id = models.ForeignKey(FranchiseTeam, to_field="lahman_fid")
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

class Park(models.Model):
	park_id = models.CharField(max_length=5,primary_key=True)
	name = models.CharField(max_length=30)
	aka = models.CharField(max_length=30)
	loc_city = models.CharField(max_length=30)
	loc_state = models.CharField(max_length=30)
	start = models.DateField()
	end = models.DateField()
	league = models.CharField(max_length="2")
	notes = models.CharField(max_length="100")

class Game(models.Model):
	game_id = models.AutoField(primary_key=True)
	date = models.DateField()
	game_type = models.IntegerField()
	day = models.CharField(max_length=3)

	visiting_team = models.ForeignKey(FranchiseTeam, to_field="retro_id")
	visiting_team_number = models.IntegerField()
	home_team = models.ForeignKey(FranchiseTeam, to_field="retro_id")
	home_team_number = models.IntegerField()

	visiting_score = models.IntegerField()
	home_score = models.IntegerField()

	length_in_outs = models.IntegerField()
	day_night = models.IntegerField()

	park_id = models.ForeignKey(Park, to_field="park_id")
	attendance = models.IntegerField()
	length_in_mins = models.IntegerField()

	v_at_bats = models.IntegerField()
	v_hits = models.IntegerField()
	v_doubles = models.IntegerField()
	v_triples = models.IntegerField()
	v_homeruns = models.IntegerField()
	v_rbis = models.IntegerField()
	v_sh = models.IntegerField()
	v_sf = models.IntegerField()
	v_hbp = models.IntegerField()
	v_walks = models.IntegerField()
	v_ibb = models.IntegerField()
	v_so = models.IntegerField()
	v_sb = models.IntegerField()
	v_cs = models.IntegerField()
	v_gdp = models.IntegerField()
	v_catcher_inter = models.IntegerField()
	v_lob = models.IntegerField()

	h_at_bats = models.IntegerField()
	h_hits = models.IntegerField()
	h_doubles = models.IntegerField()
	h_triples = models.IntegerField()
	h_homeruns = models.IntegerField()
	h_rbis = models.IntegerField()
	h_sh = models.IntegerField()
	h_sf = models.IntegerField()
	h_hbp = models.IntegerField()
	h_walks = models.IntegerField()
	h_ibb = models.IntegerField()
	h_so = models.IntegerField()
	h_sb = models.IntegerField()
	h_cs = models.IntegerField()
	h_gdp = models.IntegerField()
	h_catcher_inter = models.IntegerField()
	h_lob = models.IntegerField()

	v_pitchers_used = models.IntegerField()
	v_individual_er = models.IntegerField()
	v_team_er = models.IntegerField()
	v_wp = models.IntegerField()
	v_balks = models.IntegerField()

	h_pitchers_used = models.IntegerField()
	h_individual_er = models.IntegerField()
	h_team_er = models.IntegerField()
	h_wp = models.IntegerField()
	h_balks = models.IntegerField()

	v_putouts = models.IntegerField()
	v_assits = models.IntegerField()
	v_errors = models.IntegerField()
	v_passed_balls = models.IntegerField()
	v_dp = models.IntegerField()
	v_tp = models.IntegerField()

	h_putouts = models.IntegerField()
	h_assits = models.IntegerField()
	h_errors = models.IntegerField()
	h_passed_balls = models.IntegerField()
	h_dp = models.IntegerField()
	h_tp = models.IntegerField()

#	home_umpire
#	first_umpire
#	second_umpire
#	third_umpire
#	lf_umpire
#	rf_umpire

#	v_manager
#	h_manager

	winning_pitcher = models.ForeignKey(Player, to_field="retro_id")
	losing_pitcher = models.ForeignKey(Player, to_field="retro_id")
	saving_pitcher = models.ForeignKey(Player, to_field="retro_id")
	winning_rbi = models.ForeignKey(Player, to_field="retro_id")
	v_starter = models.ForeignKey(Player, to_field="retro_id")
	h_starter = models.ForeignKey(Player, to_field="retro_id")

	v_one = models.ForeignKey(Player, to_field="retro_id")
	v_one_pos = models.IntegerField()
	v_two = models.ForeignKey(Player, to_field="retro_id")
	v_two_pos = models.IntegerField()
	v_three = models.ForeignKey(Player, to_field="retro_id")
	v_thre_pos = models.IntegerField()
	v_four = models.ForeignKey(Player, to_field="retro_id")
	v_four_pos = models.IntegerField()
	v_five = models.ForeignKey(Player, to_field="retro_id")
	v_five_pos = models.IntegerField()
	v_six = models.ForeignKey(Player, to_field="retro_id")
	v_six_pos = models.IntegerField()
	v_seven = models.ForeignKey(Player, to_field="retro_id")
	v_seven_pos = models.IntegerField()
	v_eight = models.ForeignKey(Player, to_field="retro_id")
	v_eight_pos = models.IntegerField()
	v_nine = models.ForeignKey(Player, to_field="retro_id")
	v_nine_pos = models.IntegerField()

	h_one = models.ForeignKey(Player, to_field="retro_id")
	h_one_pos = models.IntegerField()
	h_two = models.ForeignKey(Player, to_field="retro_id")
	h_two_pos = models.IntegerField()
	h_three = models.ForeignKey(Player, to_field="retro_id")
	h_three_pos = models.IntegerField()
	h_four = models.ForeignKey(Player, to_field="retro_id")
	h_four_pos = models.IntegerField()
	h_five = models.ForeignKey(Player, to_field="retro_id")
	h_five_pos = models.IntegerField()
	h_six = models.ForeignKey(Player, to_field="retro_id")
	h_six_pos = models.IntegerField()
	h_seven = models.ForeignKey(Player, to_field="retro_id")
	h_seven_pos = models.IntegerField()
	h_eight = models.ForeignKey(Player, to_field="retro_id")
	h_eight_pos = models.IntegerField()
	h_nine = models.ForeignKey(Player, to_field="retro_id")
	h_nine_pos = models.IntegerField()

class AtBat(models.Model):
 	game_id = models.ForeignKey(Game, to_field="game_id")
	home_away =  models.CharField(max_length=30)
	inning = models.IntegerField()
	description = models.CharField(max_length=100)
	play_decription = models.CharField(max_length=10)
	hit_location = models.IntegerField()
	runners = models.CharField(max_length=10)

class Pitch(models.Model):
 	pitch_id = models.AutoField(primary_key=True) 
	pitcher = models.ForeignKey(Pitcher, to_field="pitcher_id")
 	atbat = models.ForeignKey(AtBat, to_field="atbat_id")
 	game = models.ForeignKey(Game, to_field="game_id")
 	pitch_type = models.CharField(max_length=3)
 	start_speed = models.DecimalField(max_digits=5, decimal_places=2)
 	pitch_result = models.CharField(max_length=3)
 	description = models.CharField(max_length=30)



