from numpy import mean, std

from util import process_as_dk

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

class PlayerHistory(object):

    def __init__(self, performances):
        perf_dict = {}
        for perf in performances:
            perf_dict[perf.week] = perf.points

        self.perf_dict = perf_dict
        self.history = {
            'MEAN' : mean(perf_dict.values()),
            'HIGH' : max(perf_dict.values()),
            'LOW' : min(perf_dict.values()),
            'STDEV':  std(perf_dict.values())
        }

    def __repr__(self):
        perfs = ''
        for k, v in self.perf_dict.iteritems():
            perfs += 'WEEK ' + str(k) + ' : ' + str(v)
            perfs += '\n'

        for k, v in self.history.iteritems():
            perfs += k + ' : ' + str(v) + '\n'

        return perfs
