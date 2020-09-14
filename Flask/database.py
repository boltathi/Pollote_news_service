from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads
from Flask.config import Configuration

class PyMongoDB:
    def __init__(cls):
        cls.con = None
        cls.db = None

    @classmethod
    def setDBConnection(cls,host,port):
        cls.con = MongoClient(host,int( port))
        cls.db=cls.con[Configuration.getProperty('DB_NAME')]

    @classmethod
    def getData(cls,table,key,value):
        cursor = cls.db[table].find({key:value},{'_id': False})
        return loads(dumps(cursor))

    @classmethod
    def getAllData(cls,table ):
        cursor = cls.db[table].find({}, {'_id': False})
        return loads(dumps(cursor))




    @classmethod
    def insertData(cls,table,data):
        print(cls.db[table].insert(data))

    @classmethod
    def updateData(cls,table,keyToUpdate,valueToUpdate,searchKey,searchValue,key2,value2):
        # print({"subcategory":subcategory},{"$set":{"news":"va"}},{"$set":{"category":category}})
        # cursor = cls.db.news.find({}, {'_id': False})
        # js = loads(dumps(cursor))
        # print(js)
        cls.db[table].update({searchKey:searchValue},{"$set":{keyToUpdate:valueToUpdate,key2:value2}},upsert = True)