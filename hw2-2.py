import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.students
hws = db.grades.find({"type": "homework"}).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)]);

#print grades.count()
print hws.count()

prev = -1;

for hw in hws:
	id = hw['student_id']
	if id != prev:
		# remove record
		db.grades.remove({"_id": hw['_id']})
		print "removing ", id
	else:
		print "keeping",  hw
	prev = id; 

print "records ", db.grades.count()




