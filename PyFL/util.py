def process_as_dk(pos, draft_kings_stats):
    """
    Returns DK equivalent points
    given stats from NFL API
    """
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
