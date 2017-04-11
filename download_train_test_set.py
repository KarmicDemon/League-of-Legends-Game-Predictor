### This file contains the download functions and split functions
import json
import requests as req


### Download seed data since Riot is hella stingy
### Returns one big dataset
def download_data():
    data = []

    for i in range(1, 11):
        url = 'https://s3-us-west-1.amazonaws.com/riot-developer-portal/' + \
            'seed-data/matches' + str(i) + '.json'
        print('Currently Downloading Part %d of 10 of Seed Match Dataset' % i)
        data.append(req.get(url).json())

    return data


if __name__ == '__main__':
    download_data()
