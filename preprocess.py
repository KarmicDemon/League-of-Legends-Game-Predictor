### This file contains preprocessing classes
from download import download_champion_shit, download_data

class Match(object):
    def __init__(self, tup_list):
        self.team_one = [x for x in tup_list if x[0] == 0]
        self.team_two = [x for x in tup_list if x[1] == 0]

    def __str__(self):
        i_to_c, _ = download_champion_shit()

### returns new proccessed champs
### each in ret is [[10x (team, champion_id)] , winning_team]
def turn_data_to_process():
    data = download_data()
    i_to_c = download_champion_shit()[0]

    participants = [x['participants'] for x in data]
    winners = [0 if x['teams'][0]['winner'] else 1 for x in data]

    ret = []
    for p, w in zip(participants, winners):
        _list = []
        for p2 in p:
            _list.append(((1 if p2['teamId'] == 200 else 0), \
                p2['championId']))
        ret.append((_list, w))

    print(ret)
    return ret

### retuns preprocess champs to match
def turn_process_to_match():
    proc = turn_data_to_process()
    pass
    #return [Match(x) for x in proc]
