import web
from models import Connector

urls = (
	'/', 'Index'
)

class Index:
	def __init__(self):
		self.render = web.template.render('')

		#create a new connection to the db
		self.conn = Connector('localhost',27017,'receipts','receipt')

	def GET(self, name='None'):
		#read the names from the database
		names = self.conn.read()

		#init an empty array for the store names
		a=[]
		b=[]
		c=[]
		d=[]
		e=[]

		#iterate through to get the store names and append to array
		"""for s in names:
			a.append(s['storeName'])
			b.append(s['amountCurrency'])
			c.append(s['typeOfCurrency'])
			d.append(s['date'])
			e.append(s['typeOfReceipt'])"""

		#return the render of index with the array
		return self.render.index(names)

	def POST(self,name):
		return "post"

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()