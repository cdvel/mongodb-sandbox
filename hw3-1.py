import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.school
hws = db.students.find({}).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)]);

updates = 0
for hw in hws:
 	score_list =  hw["scores"]
	low_score = 100
	for scr in score_list:
		if (scr['type'] == 'homework') and (low_score > scr['score']):
			low_score = scr['score']
	
	#print 'removing', hw['_id'], ":",  low_score
	score_list.remove({'type': 'homework', 'score': low_score})
	#print score_list
	db.students.update({'_id': hw['_id']}, {'$set': {'scores': score_list}})

print "students records ", db.students.count()

# mongo shell:
#db.students.aggregate( { '$unwind' : '$scores' } , { '$group' : { '_id' : '$_id' , 'average' : { $avg : '$scores.score' } } } , { '$sort' : { 'average' : -1 } } , { '$limit' : 1 } )


# record sample
# {
#         "_id" : 0,
#         "name" : "aimee Zank",
#         "scores" : [
#                 {
#                         "type" : "exam",
#                         "score" : 1.463179736705023
#                 },
#                 {
#                         "type" : "quiz",
#                         "score" : 11.78273309957772
#                 },
#                 {
#                         "type" : "homework",
#                         "score" : 6.676176060654615
#                 },
#                 {
#                         "type" : "homework",
#                         "score" : 35.8740349954354
#                 }
#         ]
# }

