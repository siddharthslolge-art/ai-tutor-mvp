import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection("test").document("hello").set({
    "message": "Firebase is connected!",
    "status": "success"
})

print("Document written.")

doc = db.collection("test").document("hello").get()
print("Document read:", doc.to_dict())
