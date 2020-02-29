# Server

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/Users/skinnymonkey/Desktop/LancerHacksApp/the-coalition-firebase-adminsdk-prmz5-d96882800e.json") #Replace with ur own file path
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

print("SERVER GO")


doc_ref = db.collection(u'Hi').document(u'Bye')
"""
doc_ref.set({
    u'sender': u'ur mom',
    u'message': u'lets fuck'
})
"""
doc = doc_ref.get().to_dict()
print(str(doc[u'sender']))

