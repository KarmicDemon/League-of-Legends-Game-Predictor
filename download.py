### This file contains the download functions and split functions
import json
import requests as req
import pickle
import toml

from collections import OrderedDict
from os.path import isfile
from pickle import dump, load
from preprocess import Match

int_to_champion_file = 'int_to_champion.p'
champion_to_int_file = 'champion_to_int.p'
seed_data_download_file = 'seed_data.p'
settings_toml = 'settings.toml'

### returns int_to_champion, champion_to_int
def download_champion_shit():
    int_to_champion = None
    champion_to_int = None

    if isfile(int_to_champion_file) and isfile(champion_to_int_file):
        int_to_champion = load(open(int_to_champion_file, 'rb'))
        champion_to_int = load(open(champion_to_int_file, 'rb'))
    else:
        _settings = toml.load(settings_toml)
        url = 'https://na1.api.riotgames.com/lol/static-data/v3/champions?' + \
            'api_key=' + _settings['riot_api_key']
        json_req = req.get(url).json()['data']

        champion_to_id = { x : _['id'] for x, _ in json_req.items() }
        id_to_champion = { idx : champ for champ, idx in \
            champion_to_int.items() }

        dump(champion_to_int, open(champion_to_int_file, 'wb'))
        dump(int_to_champion, open(int_to_champion_file, 'wb'))

    print(OrderedDict(sorted(int_to_champion.items())))
    return int_to_champion, champion_to_int

### Download seed data since Riot is hella stingy
### Returns one big dataset
def download_data():
    if isfile(seed_data_download_file):
        data = load(open(seed_data_download_file, 'rb'))
        return data
    else:
        data == None

        for i in range(1, 11):
            url = 'https://s3-us-west-1.amazonaws.com/riot-developer-portal/' \
                + 'seed-data/matches' + str(i) + '.json'
            print('Currently Downloading Part %d of 10 of Seed Match Dataset' \
                % i)
            json_req = req.get(url).json()
            matches = json_req['matches']

            if data == None:
                data = matches
            else:
                data = data + matches

        ### Save data to file so we never have to download again
        dump(data, open(seed_data_download_file, 'wb'))
        return data

### returns new proccessed champs
def turn_data_to_process():
    data = download_data()
    participants = [x['participants'] for x in data]

    ret = []
    for p in participants:
        _list = []
        for p2 in p:
            _list.append(((1 if p2['teamId'] == 200 else 0), \
                p2['championId']))
        ret.append(_list)

    print(ret)

### retuns preprocess champs to match
def turn_process_to_match():
    

if __name__ == '__main__':
    download_champion_shit()
    download_data()
