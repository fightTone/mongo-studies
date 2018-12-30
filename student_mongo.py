import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sample_db"]
studcol = mydb["Students"]
courses = mydb["Courses"]

stud_list = [
  { "_id": 1, "name": "John", "yr_lvl": " 1"},
  { "_id": 2, "name": "Peter", "yr_lvl": "3"},
  { "_id": 3, "name": "Amy", "yr_lvl": "3"},
  { "_id": 4, "name": "Hannah", "yr_lvl": "4"}
]

course_list = [
  { "_id": 1, "cname": "BSCS"},
  { "_id": 2, "cname": "BSCA"},
  { "_id": 3, "cname": "IT"},
  { "_id": 4, "cname": "IS"},
]

# x = studcol.insert_many(stud_list)
# y = courses.insert_many(course_list)

for x in studcol.find({},{ "_id": 0, "name": 1, "yr_lvl": 1 }):
  print(x)

for y in courses.find({},{ "_id": 0, "cname": 1}):
  print(y)