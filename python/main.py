#set encoding to UTF-8
# -*- coding: utf-8 -*-
from models import Connector

def main():
	#establish a new connection
	x = Connector('localhost',27017,'receipts','receipt')
	#create a new document for the collection
	a = {"storeName": 'Hemköp',"amountCurrency": 1260,"typeOfCurrency": 'SEK',"date": '29.10.2015',"typeOfReceipt": 'Food',"deprecated": False}
	#call the create method
	#x.create(a)
	b = {"storeName":'Pressbyrån',"typeOfReceipt":"Entertainment"}
	x.update('56eead25316a1164283b8733',b)
	#reads all current documents
	x.read()

#main method, needed for running the code for now.
if __name__ == '__main__':
	main()