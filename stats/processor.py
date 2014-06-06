from core.models import Player
import csv
from django.core.exceptions import ObjectDoesNotExist

f = open("master_14.csv", "r")

reader = csv.reader(f)

next(reader)

count = 1

for row in reader:
    count = count + 1
    if row[18] != "":
        try:
            p = Player.objects.get(retro_id=row[18])
            p.mlb_id = row[0]
            p.save()
        except ObjectDoesNotExist:
            print "woops"

    print str(count) + " of ~2500"
