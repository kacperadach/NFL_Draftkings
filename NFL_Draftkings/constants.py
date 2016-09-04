BASE_URL = 'http://api.fantasy.nfl.com/v1/players/stats?statType={}&season={}&format=json{}'

STAT_URL = 'http://api.fantasy.nfl.com/v1/game/stats?format=json'

USEFUL_DATA = ('name', 'position', 'stats', 'teamAbbr')

ALL_WEEKS = [x for x in range(1,18)]

ONE_HOUR = 3600

VALID_POSITIONS = (
    'QB',
    'RB',
    'WR',
    'TE',
    'DEF'
)

OFFENSIVE_SCORING_MULTIPLIERS = {
    5: 0.04,
    6: 4,
    7: -1,
    14: 0.1,
    15: 6,
    20: 1,
    21: 0.1,
    22: 6,
    28: 6,
    29: 6,
    30: -1,
    32: 2,
    45: 1,
    46: 2,
    47: 2,
    49: 2,
    50: 6,
    51: 2,
    53: 6
}

DEFENSIVE_SCORING_MULTIPLIERS = {
    45: 1,
    46: 2,
    47: 2,
    49: 2,
    50: 6,
    51: 2,
    53: 6,
}