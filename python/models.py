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
			db = client[dbname]
			collection = db[collectionname]
			print(db.collection.count())
		except pymongo.errors.ConnectionFailure, e:
			print("problem connecting to MongoDB: %s" % e)
		finally:
			print("connected to mongodb")
		

	#create the four pillars of db based programming, CRUD
	#TODO: methods with variable argument number for working with all collections
	def create(self, storename, amount, currency, date, typeOf, deprecated):
		#define data to insert
		v = {"storeName": storename,"amountCurrency": amount,"typeOfCurrency": currency,"date": currency,"typeOfReceipt": typeOf,"deprecated": deprecated}
		#insert into collection
		try:
			#try inserting the document into the database
			collection.insert(v)
		except pymongo.error.OperationFailure, e:
			print("Error code: %s" % e)

	def read(self):
		#read the data from collection
		data = collection.find()

		#iterate through the data and print to console for now
		for row in data:
			print(row)
	
	def update():
		return 0
	
	def delete(): 
		return 0

def main():
	#establish a new connection
	x = Connector('localhost',27017,'receipts','receipt')

	#creates a new document for inserting
	x.create('ICA Maxi', 556, 'SEK', '21.01.2016','Food',False)

	#reads all current documents
	x.read()

if __name__ == '__main__':
	main()


"""MongoDB stores data in JSON format. MongoDB is a nosql language, meaning it is not relational. The structure is documentational,
 no objects are stored, rather documents are stored in a collection that is in turn stored in a database."""
