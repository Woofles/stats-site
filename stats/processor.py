from core.models import Player
import csv
from django.core.exceptions import ObjectDoesNotExist

f = open("playerid_list.csv", "r")
out = open("newplayers.txt","w")

reader = csv.reader(f)

next(reader)

count = 1

for row in reader:
    count = count + 1
    if row[5] != "NULL" and row[4] != "NULL":
        try:
            p = Player.objects.get(retro_id=row[5])
            p.mlb_id = row[4]
            p.save()
        except ObjectDoesNotExist:
            p = Player(last_name=row[0],first_name=row[1],mlb_id=row[4],retro_id=row[5])
            p.save()
            out.write(p.first_name + " - " + p.last_name + " - " + p.mlb_id + "\n")

    print str(count) + " of ~80000"
