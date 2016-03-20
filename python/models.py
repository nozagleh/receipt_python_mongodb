#set encoding to UTF-8
# -*- coding: utf-8 -*-
#import mongoclient from pymongo library
from pymongo import MongoClient
from bson.objectid import ObjectId

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

	#method takes in a whole document
	def create(self, document):
		#insert into collection
		try:
			#try inserting the document into the database
			collection.insert(document)
		except pymongo.error.OperationFailure, e:
			print("Error code: %s" % e)

	def read(self):
		#read the data from collection
		data = collection.find()
		result = []
		#iterate through the data and print to console for now
		for row in data:
			result.append(row)
			#print(a)
			#print row
		return result
	
	def update(self, id, document):
		try:
			print(document)
			collection.update({'_id': ObjectId(id)},
				{'$set': document})
		except pymongo.error.OperationFailure, e:
			print("Error code: %s" % e)
	
	def delete(): 
		return 0




"""MongoDB stores data in JSON format. MongoDB is a nosql language, meaning it is not relational. The structure is documentational,
 no objects are stored, rather documents are stored in a collection that is in turn stored in a database."""
