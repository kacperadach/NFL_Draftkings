from constants import USEFUL_DATA, VALID_POSITIONS

def process_json_data(data, name=None, team=None):
    data = _remove_non_offensive_players(data)
    if name and not team:
        return _extract_player(data, name)
    elif team and not name:
        return _extract_team(data, team)
    elif not team and not name:
        return _extract_all_players(data)
    else:
        return _extract_player(_extract_team(data, team), name)

def _extract_team(data, team):
    filtered_data = []
    for player in data:
        if team == player['teamAbbr']:
            filtered_data.append(_remove_useless_data(player))
    return filtered_data

def _extract_player(data, name):
    filtered_data = []
    for player in data:
        if name in player['name']:
            filtered_data.append(_remove_useless_data(player))
            break
    return filtered_data

def _extract_all_players(data):
    filtered_data = []
    for player in data:
        filtered_data.append(_remove_useless_data(player))
    return filtered_data

def _remove_useless_data(data):
    filtered_data = {}
    for key, val in data.items():
        if key in USEFUL_DATA:
            filtered_data[key] = val
    return filtered_data

def _remove_non_offensive_players(data):
    filtered_data = []
    for player in data:
        if player['position'] in VALID_POSITIONS:
            filtered_data.append(player)
    return filtered_data
