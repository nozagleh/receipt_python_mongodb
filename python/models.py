#import mongoclient from pymongo library
from pymongo import MongoClient

#set client as new connection
client = MongoClient('localhost',25042);

#set db as the Mongo DB
db = client.nameOfDatabase;
#set collection from database
coll = db.nameOfDatabase;

"""MongoDB stores data in JSON format. MongoDB is a nosql language, meaning it is not relational. The structure is documentational,
 no objects are stored, rather documents are stored in a collection that is in turn stored in a database."""
