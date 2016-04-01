import web
from models import Connector
import pymongo

urls = (
	'/', 'Index',
	'/r/(.+)', 'r'
)

render = web.template.render('/templates')

class Index:
	def __init__(self):

		#create a new connection to the db
		self.conn = Connector('localhost',27017,'receipts','receipt')

	def GET(self, name='None'):
		#read the names from the database
		names = self.conn.read()

		#return the render of index with the array
		return render.index(names)

	def POST(self,name):
		return "post"

#start of class for getting the individual pages for receipts based on an array of id's
class r:
	def GET(self,rname):
		conn = Connector('localhost',27017,'receipts','receipt')
		temparr = conn.read()
		arr = []
		for x in temparr:
			arr.append(str(x['_id']))

		for v in arr:
			if (rname == v):
				return "Hello World! %s" % rname
		return arr
		#return render.index()

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()