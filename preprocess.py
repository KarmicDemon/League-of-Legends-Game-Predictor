### This file contains preprocessing classes

class Match(object):
    def __init__(self, tup_list):
        self.team_one = [x for x in tup_list if x[0] == 0]
        self.team_two = [x for x in tup_list if x[1] == 0]

    def __str__(self):
        i_to_c, _ = download_champion_shit()

### returns new proccessed champs
def turn_data_to_process():
    data = download_data()
    i_to_c = download_champion_shit()[0]

    participants = [x['participants'] for x in data]

    ret = []
    for p in participants:
        _list = []
        for p2 in p:
            _list.append(((1 if p2['teamId'] == 200 else 0), \
                i_to_c[p2['championId']]))
        ret.append(_list)

    print(ret)

### retuns preprocess champs to match
def turn_process_to_match():
    proc = turn_data_to_process()
    pass
    #return [Match(x) for x in proc]
