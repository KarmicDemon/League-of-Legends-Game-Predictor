### This file contains preprocessing classes
import numpy as np

from download import download_champion_shit, download_data

def arg_find(arg, _list):
    for idx, val in enumerate(_list):
        if val == arg:
            return idx

### returns new proccessed champs
### each in ret is [[10x (team, champion_id)] , winning_team]
def turn_data_to_process():
    data = download_data()
    i_to_c = download_champion_shit()[0]

    participants = [x['participants'] for x in data]
    targets = [0 if x['teams'][0]['winner'] else 1 for x in data]

    pre_ret = []
    features = []

    arg_list = sorted(list(i_to_c.copy().keys()))
    num_champs = len(list(i_to_c.copy().keys()))

    for p in participants:
        _list = []
        for p2 in p:
            _list.append(arg_find(int(p2['championId']), arg_list))
        pre_ret.append(_list)

    for p in pre_ret:
        hi = p[:5]
        pi = p[5:]

        team_one = [0] * num_champs
        team_two = [0] * num_champs


        for _ in hi:
            team_one[(_ - 1)] = 1

        for _ in pi:
            team_one[(_ - 1)] = 1

        yo = team_one + team_two
        features.append(yo)

    # return features, targets
    return BatchService(features, targets)


### create batch object
def get_nn_x_y():
    return turn_data_to_process()



class BatchService(object):
    def __init__(self, inputs, outputs):
        self.data_inputs = inputs
        self.data_outputs = outputs
        self.num_examples = len(self.data_inputs)

        self.index = 0

    def get_batch(self, batch_size):
        start = self.index
        end = batch_size + self.index

        if (end > self.num_examples):
            self.index = batch_size
            start = 0
            end = batch_size

        self.index = end

        x = np.array(self.data_inputs[start:end])
        y = np.array(self.data_outputs[start:end])

        #y = np.transpose(y)

        return x, y

if __name__ == '__main__':
    # turn_data_to_process()
    pass
