import logging
import os
import time
from pymongo import MongoClient
import pprint
from api import load_current_values, CONFIG

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO)
logging.info('main started')


if ("MONGO_URI" in os.environ):
    client = MongoClient(os.environ["MONGO_URI"])
else:
    client = MongoClient()

db = client.osrs_api
table = db.experience_history
logging.info(f'CONFIG loaded {CONFIG}')

stop = False
while not stop:
    for player in CONFIG['players']:
        logging.debug(f'loading values for player {player}')
        values = []

        try:
            values = load_current_values(player)
        except Exception as e:
            logging.error(e)
            
        # get current in db
        for val in values:
            skill = val['name']
            key = 'experience' if val['type'] == 'skill' else 'kc'
            vals = table.find_one({'player': player, 'name': skill, key: val[key]}, sort=[('request_date', -1)])
            if vals is None:
                logging.info(f'no data found for skill {skill} and {key} {val[key]} and player {player}, inserting new val')
                table.insert_one(val)
            elif (vals['request_date'] > val['request_date']):
                request_date = val['request_date']
                logging.info(f'value found {vals} with newer request date ({request_date}), updating')
                table.update_one(
                    {'_id': vals['_id']},
                    {
                        '$set': {
                            'request_date': request_date
                        }
                    })
            else:
                logging.debug(f'nothing to do on skill {skill}')
            
    
    pooling_interval_seconds = CONFIG['pooling_interval_seconds']
    logging.info(f'waiting {pooling_interval_seconds} seconds')
    time.sleep(pooling_interval_seconds)


logging.info('ending')