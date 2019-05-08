"""
user:long
"""
from pymongo import MongoClient


class DbUtil:
    host = '192.168.1.10'
    port = 27017
    db_user = 'job'
    db_pass = 'job'
    instance = None

    def __init__(self):
        """
        单例连接
        """
        if self.instance is None:
            self.instance = MongoClient(self.host, self.port)
        pass

    def get_instance(self):
        """
        获取数据库对象
        :return:
        """
        return self.instance

    def insert(self, data=None, select_db='jobs', select_collection='jobs'):
        """
        新增
        :param data:
        :param select_db:
        :param select_collection:
        :return:
        """
        db_ = self.instance[select_db]

        if self.db_user and self.db_pass:
            db_.authenticate(self.db_user, self.db_pass)

        if isinstance(data, list):
            return db_[select_collection].insert_many(data)
        else:
            return db_[select_collection].insert_one(data)

if __name__ == '__main__':
    """
    test
    """
    db = DbUtil()
    insert = db.insert({'abc': 123})
    print('success :', insert.inserted_id)
