#import mongoclient from pymongo library
from pymongo import MongoClient

class Connector:
	#initilize variables
	#servername, portnr, dbname, collectionname, client, db, collection

	#define init method with no arguments

	#define init method that takes servername and portnr as arguments
	def __init__(self, servername = 'localhost', portnr = 27017, dbname = 'test', collectionname = 'testcollection'):
		#set servername and portnr
		self.servername = servername
		self.portnr = portnr
		self.dbname = dbname
		self.collectionname = collectionname
		try:
			client = MongoClient(servername,portnr)
			db = dbname
			collection = collectionname
		except Exception, e:
			print("problem")
		finally:
			print("connected to mongodb")
		

	#create the four pillars of db based programming, CRUD
	def create():
		return 0
	def read():
		return 0
	def update():
		return 0
	def delete(): 
		return 0

x = Connector()


"""MongoDB stores data in JSON format. MongoDB is a nosql language, meaning it is not relational. The structure is documentational,
 no objects are stored, rather documents are stored in a collection that is in turn stored in a database."""
