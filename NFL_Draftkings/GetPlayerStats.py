from GatherPlayerData import gather_json
from ProcessPlayerStats import process_json_data
from constants import ALL_WEEKS

def get_player_stats(name=None, position=None, team=None, week=None, season=None):
    data = gather_json(week=week, season=season, position=position)
    return process_json_data(data, name=name, team=team)

def get_weekly_player_stats(name=None, position=None, team=None, weeks=None, season=None):
    weekly_data = []
    if not weeks:
        weeks = ALL_WEEKS
    for w in weeks:
        week_dict = get_player_stats(name=name, position=position, team=team, week=w, season=season)
        if week_dict:
            for p in week_dict:
                p['week'] = w
                weekly_data.append(p)
    return weekly_data
