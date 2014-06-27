from core.models import Player
import shlex

season_stats_fields = [
    'games',
    'games played'
    'plate appearances',
    'PAs',
    'at bats',
    'abs',
    'runs',
    'hits',
    'doubles',
    'triples',
    'home runs',
    'hrs',
    'runs batted in',
    'rbis',
]

daily_stats_fields = [
    'nope',
]

return_value = {
    "message": "",
    "data": None,
}

context = {}

def parse_input(inp):

    shl = shlex.shlex(inp)
    return entrance(shl)
    # return return_value

def entrance(shl):
    token = peek(shl).lower()
    if token == "compare":
        pass
    elif token == "plot":
        pass
    else:
        return first_name(shl)

def first_name(shl):
    token = shl.get_token().lower()
    players = Player.objects.filter(first_name=token)
    if len(players) > 0:
        context['first_name'] = token
        return last_name(shl)
    else:
        #no first name or spelled incorrectly
        return "couldn't parse input - no first name"

def last_name(shl):
    global context
    token = shl.get_token().lower()
    players = Player.objects \
                .filter(first_name=context['first_name']) \
                .filter(last_name=token)
    context['player'] = players[0]
    if len(players) > 0:
        if season_stats_fields.count(peek(shl)) > 0:
            return season_stats(shl)
        elif daily_stats_fields.count(peek(shl)) > 0:
            return daily_stats(shl)
        else:
            #didn't get stat next
            return "couldn't parse input - invalid stats"
    else:
        #no last name or spelled incorrectly
        return "couldn't parse input - no last name"

def season_stats(shl):
    global context
    token = shl.get_token().lower()
    context['stat'] = token
    token = shl.get_token().lower()
    try:
        num_token = float(token)
        context['season'] = context['player'].batterseason_set.get(season=num_token)
    except ValueError:
        return "no year supplied"
    season = context['season']
    stat = context['stat']
    if stat == "games" or stat == "games played":
        return season.games
    elif stat == "rbis":
        return season.rbis
    elif stat == "runs":
        return season.runs
    elif stat == "hits":
        return season.hits
    elif stat == "singles":
        return season.singles
    elif stat == "doubles":
        return season.doubles
    elif stat == "triples":
        return season.triples
    elif stat == "hrs":
        return season.home_runs
    return token

def daily_stats(shl):
    pass


def peek(shl):
    token = shl.get_token().lower()
    shl.push_token(token)
    return token
