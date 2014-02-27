from flask_login import UserMixin
from pymongo import MongoClient

mongo = MongoClient()
db = mongo.xci

class User(UserMixin):
    def __init__(self, userid, password):
        self.id = userid
        self.password = password

    def get_id(self):
        try:
            user = db.userprofiles.find_one({"username":self.id})
            return unicode(self.id)
        except Exception, e:
            raise e

def getUserProfile(userid):
    return db.userprofiles.find_one({'username':userid})

def saveUserProfile(profile, userid=None):
    if userid:
        updateUserProfile(profile, userid)
    else:
        db.userprofiles.insert(profile)

def updateUserProfile(profile, userid):
    db.userprofiles.update({'username':userid}, profile, manipulate=False)

def saveCompetency(json_comp):
    if getCompetency(json_comp['uri']):
        updateCompetency(json_comp)
    else:
        db.competency.insert(json_comp, manipulate=False)

def updateCompetency(json_comp):
    db.competency.update({'uri':json_comp['uri']}, json_comp, manipulate=False)

def getCompetency(uri, objectid=False):
    if objectid:
        return db.competency.find_one({'uri':uri})
    return db.competency.find_one({'uri':uri}, {'_id':0})

def findoneComp(d):
    return db.competency.find_one(d)

def findCompetencies(d=None):
    return [x for x in db.competency.find(d)]

def findCompetencyFrameworks(d=None):
    return [x for x in db.compfwk.find(d)]

def saveCompetencyFramework(json_fwk):
    if getCompetencyFramework(json_fwk['uri']):
        updateCompetencyFramework(json_fwk)
    else:
        db.compfwk.insert(json_fwk, manipulate=False)

def updateCompetencyFramework(json_fwk):
    db.compfwk.update({'uri':json_fwk['uri']}, json_fwk, manipulate=False)

def getCompetencyFramework(uri):
    return db.compfwk.find_one({'uri':uri})

def savePerformanceFramework(json_fwk):
    if getPerformanceFramework(json_fwk['uri']):
        updatePerformanceFramework(json_fwk)
    else:
        db.perfwk.insert(json_fwk, manipulate=False)

def updatePerformanceFramework(json_fwk):
    val = db.perfwk.update({'uri':json_fwk['uri']}, json_fwk, manipulate=False)

def getPerformanceFramework(uri):
    return db.perfwk.find_one({'uri':uri})

def findPerformanceFrameworks(d=None):
    return [x for x in db.perfwk.find(d)]

def dropCompCollections():
    db.drop_collection('competency')
    db.drop_collection('compfwk')
    db.drop_collection('perfwk')

def dropAll():
    return mongo.drop_database(db)





# from bson.objectid import ObjectId

# # The web framework gets post_id from the URL and passes it as a string
# def get(post_id):
#     # Convert from string to ObjectId:
#     document = client.db.collection.find_one({'_id': ObjectId(post_id)})