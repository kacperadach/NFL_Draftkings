from ConvertToDraftKings import convert_to_DK
from GetPlayerStats import get_player_stats, get_weekly_player_stats

def get_scores(name=None, position=None, team=None, week=None, season=None):
    data = get_player_stats(name=name, position=position, team=team, week=week, season=season)
    for d in data:
        d['stats'] = convert_to_DK(d)
    return data

def get_weekly_scores(name=None, position=None, team=None, weeks=None, season=None):
    weekly_data = get_weekly_player_stats(name=name, position=position, team=team, weeks=weeks, season=season)
    for wd in weekly_data:
       wd['stats'] = convert_to_DK(wd)
    return weekly_data

def get_top_performers(position=None, team=None, week=None, season=None, top=10):
    data = get_scores(position=position, team=team, week=week, season=season)
    newlist = sorted(data, key=lambda k: k['stats'], reverse=True)
    return newlist[0:top]
