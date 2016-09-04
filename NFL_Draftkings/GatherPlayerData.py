from json import loads
from datetime import datetime

from requests import get
from requests_cache import install_cache

from constants import VALID_POSITIONS, BASE_URL, ONE_HOUR

install_cache('nfl_api_cache', expire_after=ONE_HOUR)

def gather_json(week=None, season=None, position=None):
    nfl_api_url = _format_url(week, season, position)
    try:
        response = get(nfl_api_url)
        return loads(response.text)['players']
    except:
        raise Exception('Error retrieving data from NFL api')

def _format_url(week, season, position):
    type = 'weekStats'
    if not season:
        season = _get_default_season()
    if not week:
        type = 'seasonStats'
        week_string = ''
    else:
        week_string = '&week={}'.format(week)
    nfl_api_url = BASE_URL.format(type, season, week_string)
    if position in VALID_POSITIONS:
        nfl_api_url += '&position=' + position
    return nfl_api_url

def _get_default_season():
    today = datetime.today()
    if today.month < 9:
        return today.year - 1
    else:
        return today.year
