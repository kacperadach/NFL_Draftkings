from constants import OFFENSIVE_SCORING_MULTIPLIERS, DEFENSIVE_SCORING_MULTIPLIERS

def convert_to_DK(data):
    if data['position'] == 'DEF':
        return _get_defensive_scoring(data['stats'])
    else:
        return _get_offensive_scoring(data['stats'])

def _get_offensive_scoring(data):
    return round(_get_offensive_conditional_scoring(data) + _get_offensive_multiplier_scoring(data), 1)

def _get_defensive_scoring(data):
    return round(_get_defensive_conditional_scoring(data) + _get_defensive_multiplier_scoring(data), 1)

def _get_offensive_multiplier_scoring(data):
    points = 0
    for key, val in data.items():
        try:
            points += int(val) * OFFENSIVE_SCORING_MULTIPLIERS[int(key)]
        except KeyError:
            continue
    return points

def _get_defensive_multiplier_scoring(data):
    points = 0
    for key, val in data.items():
        try:
            points += int(val) * DEFENSIVE_SCORING_MULTIPLIERS[int(key)]
        except KeyError:
            continue
    return points

def _get_offensive_conditional_scoring(data):
    points = 0
    if '5' in data and int(data['5']) >= 300:
        points += 3
    if '14' in data and int(data['14']) >= 100:
        points += 3
    if '21' in data and int(data['21']) >= 100:
        points += 3
    return points

def _get_defensive_conditional_scoring(data):
    points = 0
    points_allowed = 0 if '54' not in data else int(data['54'])
    if points_allowed == 0:
        points += 10
    elif 1 <= points_allowed <= 6:
        points += 7
    elif 7 <= points_allowed <= 13:
        points += 4
    elif 14 <= points_allowed <= 20:
        points += 1
    elif 28 <= points_allowed <= 34:
        points -= 1
    elif 35 <= points_allowed:
        points -= 4
    return points
