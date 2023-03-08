from pymongo import MongoClient
from pprint import pprint


def my_foo():
    pass


if __name__ == '__main__':
    MONGO_URL = 'mongodb://mongo:27017'
    client = MongoClient(MONGO_URL)
    db = client.admin
    dbs_list = db.command('listDatabases')
    pprint(dbs_list)
    print('End')

