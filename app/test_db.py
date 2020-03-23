import pymongo


client = pymongo.MongoClient()

db = client.xscan

docs = db.docs
imgs = db.imgs
