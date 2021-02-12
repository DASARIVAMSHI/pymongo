import pymongo as p
myclient = p.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabases"]
mycol=mydb["courses"]
#mydict={"name":"vamshi","address":"vijayawada"}
#newvalues={"$set":{"address":"hyderabad"}}
#x=mycol.insert_one(mydict,newvalues)
#x=mycol.update_one(mydict,newvalues)
#x=mycol.delete_one(mydict)
x=mycol.drop()

print(x)