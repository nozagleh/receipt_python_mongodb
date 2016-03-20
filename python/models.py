#import mongoclient from pymongo library
from pymongo import MongoClient

class Connector:
	#initilize variables

	#define init method with no arguments

	#define init method that takes servername and portnr as arguments
	def __init__(self, servername = 'localhost', portnr = 27017, dbname = 'test', collectionname = 'testcollection'):
		print(servername + ";" + str(portnr) + ";" + dbname + ";" + collectionname + ";")

		global client
		global db
		global collection

		try:
			client = MongoClient(servername,portnr)
			db = client['test']
			collection = db['testcollection']
			print(db.collection.count())
		except pymongo.errors.ConnectionFailure, e:
			print("problem connecting to MongoDB: %s" % e)
		finally:
			print("connected to mongodb")
		

	#create the four pillars of db based programming, CRUD

	def create(self):
		#define data to insert
		v = {'x':42}
		#insert into collection
		collection.insert(v)

	def read(self):
		#read the data from collection
		data = collection.find()

		#iterate through the data and print to console
		for row in data:
			print(row)
	
	def update():
		return 0
	
	def delete(): 
		return 0

x = Connector()
print(x.read())
#print(x.create())


"""MongoDB stores data in JSON format. MongoDB is a nosql language, meaning it is not relational. The structure is documentational,
 no objects are stored, rather documents are stored in a collection that is in turn stored in a database."""
