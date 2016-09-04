import unittest

from NFL_Draftkings.GetPlayerDKScores import *

class TestPublicApiMethods(unittest.TestCase):

    def test_get_stats_empty(self):
        data = get_stats(season=2015)
        assert len(data) == 585

    def test_get_stats_name(self):
        data = get_stats(name='Tom Brady', season=2015)
        assert len(data) == 1 and data[0]['name'] == 'Tom Brady'

    def test_get_stats_name_and_week(self):
        data = get_stats(name='Tom Brady', week=1, season=2015)
        assert len(data) == 1 and data[0]['name'] == 'Tom Brady'

    def test_get_stats_position(self):
        data = get_stats(position='QB', season=2015)
        assert len(data) == 72 and not [x for x in data if x['position'] != 'QB']

    def test_get_stats_position_and_week(self):
        data = get_stats(position='QB', week=1, season=2015)
        assert len(data) == 35 and not [x for x in data if x['position'] != 'QB']

    def test_get_stats_position_and_week_and_name_and_team(self):
        data = get_stats(name='Tom Brady', position='QB', team='NE', week=1, season=2015)
        assert len(data) == 1 and not [x for x in data if x['position'] != 'QB']

    def test_get_weekly_stats_empty(self):
        data = get_weekly_stats(season=2015)
        assert len(data) == 5960

    def test_get_weekly_stats_name(self):
        data = get_weekly_stats(name='Tom Brady', season=2015)
        assert len(data) == 16 and not [x for x in data if x['name'] != 'Tom Brady']

    def test_get_weekly_stats_name_and_weeks(self):
        data = get_weekly_stats(name='Tom Brady', weeks=[1,2,3], season=2015)
        assert len(data) == 3 and not [x for x in data if x['name'] != 'Tom Brady']

    def test_get_weekly_stats_position(self):
        data = get_weekly_stats(position='WR', season=2015)
        assert len(data) == 2170 and not [x for x in data if x['position'] != 'WR']

    def test_get_weekly_stats_position_and_week(self):
        data = get_weekly_stats(position='WR', weeks=[1,2,3], season=2015)
        assert len(data) == 402 and not [x for x in data if x['position'] != 'WR']

    def test_get_weekly_stats_position_and_week_and_name_and_team(self):
        data = get_weekly_stats(name='Julian Edelman', position='WR', team='NE', weeks=[1,2,3], season=2015)
        assert len(data) == 3 and not [x for x in data if x['name'] != 'Julian Edelman']

    def test_get_top_performers_empty(self):
        data = get_top_performers(season=2015)
        assert len(data) == 10 and data[0]['name'] == 'Cam Newton'

    def test_get_top_performers_position(self):
        data = get_top_performers(position='RB', season=2015)
        assert len(data) == 10 and not [x for x in data if x['position'] != 'RB']

    def test_get_top_performers_team(self):
        data = get_top_performers(team='NE', season=2015)
        assert len(data) == 10 and not [x for x in data if x['teamAbbr'] != 'NE']

    def test_get_top_performers_week(self):
        data = get_top_performers(week=1, season=2015)
        assert len(data) == 10 and data[0]['name'] == 'Julio Jones'

    def test_get_top_performers_top_15(self):
        data = get_top_performers(top=15, season=2015)
        assert len(data) == 15 and data[0]['name'] == 'Cam Newton'

if __name__ == '__main__':
    unittest.main()