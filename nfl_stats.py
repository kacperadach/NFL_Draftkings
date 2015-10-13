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

    def __init__(self, info):
        self.name = info['name']
        self.pos = info['position']
        self.points = self.calc_points(info)

    def __repr__(self):
        return "{0} {1}".format(self.name, self.points)

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

def get_top_performances(week, position='QB', top_take=5):
    data = gather_json(week, position)
    all_players = []
    for player_info in data['players']:
        all_players.append(Player(player_info))
    for player in sorted(all_players, 
                         key=lambda x: x.points, reverse=True)[0:top_take]:
        print player

def get_player_points(player_name, week, position=None):
    data = gather_json(week)

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

    return points
