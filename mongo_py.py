import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]#db_name
mycol = mydb["customers"]#tables

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]


try:
	print("yo!")
	#uncomment to insert
	x = mycol.insert_many(mylist)
	#print list of the _id values of the inserted documents:
	print(x.inserted_ids)
except:
	print("mylist already exist!")

#find only one
x = mycol.find_one()
print(x)

# #loop and print without id
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x)

# #loop and print all without address
# for x in mycol.find({},{ "address": 0 }):
#   print(x)


#search query by address
# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

#Find documents where the address starts with the letter "S" or higher:
# myquery = { "address": { "$gt": "S" } }
# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

#Find documents where the address starts with the letter "S":
# myquery = { "address": { "$regex": "^S" } }
# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

# Sort the result alphabetically by name:
#-----> sort("name", 1) #ascending
#-----> sort("name", -1) #descending
# mydoc = mycol.find().sort("name")
# for x in mydoc:
#   print(x)

# #Delete the document with the address "Mountain 21":
# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)

# #Delete all documents were the address starts with the letter S:
# myquery = { "address": {"$regex": "^S"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")

#Delete all documents in the "customers" collection:
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")

#Dtop collection
#mycol.drop()

#Change the address from "Valley 345" to "Canyon 123":
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
#print "customers" after the update:
for x in mycol.find():
  print(x)