from urllib2 import Request, urlopen, URLError
import json

valid_positions = (
    'QB',
    'RB',
    'WR',
    'TE',
    'DEF'
)

class Player(object):

    def __init__(self, info, week):
        self.name = info['name']
        self.pos = info['position']
        self.team = info['teamAbbr']
        self.points = self.calc_points(info)
        self.week = week

    def __repr__(self):
        return "{0} {1} {2} {3}".format(self.name, self.points, self.team, self.week)

    def calc_points(self, stats):
        draft_kings_stats = {}
        if stats is None:
            print 'player not found in data'
            return None
        else:
            for x in xrange(91):
                try:
                    num_str = str(x)
                    draft_kings_stats[num_str] = stats['stats'][num_str]
                except KeyError:
                    draft_kings_stats[num_str] = '0'

        return process_as_dk(self.pos, draft_kings_stats)  

def gather_json(week, position=None):
    baseurl = 'http://api.fantasy.nfl.com/v1/players/stats?statType=weekStats&season=2015&format=json&week='
    week = str(week)
    url = baseurl + week
    if position in valid_positions:
        url = url + '&position=' + position
    try:
        response = urlopen(Request(url))
        return json.loads(response.read())
    except URLError, e:
        raise Exception('Incorrect parameters, could not load data')


def get_top_performances(week, position=None, top_take=5, team=None):
    data = gather_json(week, position)
    all_players = []
    for player_info in data['players']:
        all_players.append(Player(player_info, week))

    for player in sorted(all_players, key=lambda x: x.points, reverse=True):
        if team is not None:
            if player.team == team:
                print player
                top_take -= 1
        else:
            print player
            top_take -= 1

        if top_take == 0:
            break


def get_player_points(player_name, week, position=None):
    data = gather_json(week)

    stats = None
    for player in data['players']:
        if player_name in player['name']:
            stats = player
            pos = player['position']
            break

    draft_kings_stats = {}
    if stats is None:
        print 'player not found in data'
        return None
    else:
        for x in xrange(91):
            try:
                num_str = str(x)
                draft_kings_stats[num_str] = stats['stats'][num_str]
            except KeyError:
                draft_kings_stats[num_str] = '0'

    return process_as_dk(pos, draft_kings_stats)

def get_player_week_by_week(player_name, end_week, position=None):

    for x in range(end_week):
        data = gather_json(x+1, position)
        for player_info in data['players']:
            if player_name in player_info['name']:
                player = Player(player_info, x+1)
                print player
                break

def process_as_dk(pos, draft_kings_stats):
    points = 0
    if pos != 'DEF':
        points += (int(draft_kings_stats['6']) * 4)
        points += (int(draft_kings_stats['5']) * 0.04)
        if int(draft_kings_stats['5']) >= 300:
            points += 3
        points -= (int(draft_kings_stats['7']) * 1)
        points += (int(draft_kings_stats['14']) * 0.1)
        points += (int(draft_kings_stats['15']) * 6)
        if int(draft_kings_stats['14']) >= 100:
            points += 3
        points += (int(draft_kings_stats['21']) * 0.1)
        points += (int(draft_kings_stats['20']) * 1)
        points += (int(draft_kings_stats['22']) * 6)
        if int(draft_kings_stats['21']) >= 100:
            points += 3
        points += (int(draft_kings_stats['28']) * 6)
        points -= (int(draft_kings_stats['30']) * 1)
        points += (int(draft_kings_stats['32']) * 2)
        points += (int(draft_kings_stats['29']) * 6)
    elif pos == 'DEF':
        points += (int(draft_kings_stats['45']) * 1)
        points += (int(draft_kings_stats['46']) * 2)
        points += (int(draft_kings_stats['47']) * 2)
        points += (int(draft_kings_stats['53']) * 6)
        points += (int(draft_kings_stats['50']) * 6)
        points += (int(draft_kings_stats['49']) * 2)
        points += (int(draft_kings_stats['51']) * 2)

        points_allowed = int(draft_kings_stats['54'])
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
    else:
        print 'Invalid position'
    return points
