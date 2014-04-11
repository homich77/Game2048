__author__ = 'user'
import redis
import pickle

class SqlManager(object):
    def __init__(self):
        self.POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

    '''def get(key):
        value = connection.get(key)
        '''

    def set(self, key, board):
        self.connection = redis.StrictRedis(connection_pool=self.POOL)
        if self.connection.set(key, pickle.dumps(board)):
            print 'Board was saved'

    def get(self, key):
        self.connection = redis.StrictRedis(connection_pool=self.POOL)
        return pickle.loads(self.connection.get(key))
