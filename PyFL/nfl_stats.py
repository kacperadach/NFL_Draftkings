from urllib2 import Request, urlopen, URLError
import json

from player import Player, PlayerHistory
from constants import *
from util import process_as_dk


def gather_json(week, position=None):
    """
    Utility method for acquiring json data from NFL api
    """
    week = str(week)
    url = baseurl + week
    if position in valid_positions:
        url = url + '&position=' + position
    try:
        response = urlopen(Request(url))
        return json.loads(response.read())
    except URLError, e:
        raise Exception('Incorrect parameters, could not load data')


def get_top_performances(week, position=None, team=None, top_take=5):
    """
    Get the top performances for a certain week, can be specified by position and team

    Example:
        get_top_performances(4, team='NE', top_take=10)
    """
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
    """
    Get a player's points for a certain week

    Example:
        get_player_points('Tom Brady', 1, position='QB')
    """
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
    """
    Get a player's scores week by week along with a min, max, stdev and mean
    
    Example:
        get_player_week_by_week('Tom Brady', 10, position='QB')

    """
    player_history = []
    for x in range(end_week):
        data = gather_json(x+1, position)
        for player_info in data['players']:
            if player_name in player_info['name']:
                player_history.append(Player(player_info, x+1))
                break

    return PlayerHistory(player_history)
