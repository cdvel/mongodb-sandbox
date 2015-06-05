import bottle 
import pymongo

@bottle.route('/')
def indef():
	
	# connect to mongoDB
	connection = pymongo.MongoClient('localhost', 27017)

	#attach to test db
	db = connection.test

	# get handle to names collection
	names = db.names

	# find a single doc
	item = names.find_one()

	return '<b> Hello %s </b>' % item['name']

bottle.run(host='localhost', port=8080)
