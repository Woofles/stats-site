from core.models import Player
import csv

f = open("playerid_list.csv", "r")

reader = csv.reader(f)

for row in reader:
    if row[5] != "NULL" and row[4] != "NULL":
        p = Player.objects.get(retro_id=row[5])
        # print p.last_name
