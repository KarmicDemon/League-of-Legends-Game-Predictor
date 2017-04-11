### This file contains the download functions and split functions
import json
import requests as req
import pickle

from os.path import isfile
from pickle import dump, load

seed_data_download_file = 'seed_data.p'

### Download seed data since Riot is hella stingy
### Returns one big dataset
def download_data():
    data = None

    if isfile(seed_data_download_file):
        data = load(open(seed_data_download_file, 'rb'))
    else:
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


if __name__ == '__main__':
    data = download_data()
    print(data[1]['timeline'])
