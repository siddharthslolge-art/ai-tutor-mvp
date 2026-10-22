import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def company_employees(company_id):
    return db.collection("companies").document(company_id).collection("employees")

def test_per_company_data():
    # 1. Write test data for two companies
    company_employees("acme").document("e1").set({"name": "Asha", "role": "analyst"})
    company_employees("acme").document("e2").set({"name": "Ravi", "role": "engineer"})
    company_employees("globex").document("e3").set({"name": "Mia", "role": "analyst"})

    # 2. Query: only analysts in acme
    results = company_employees("acme").where("role", "==", "analyst").stream()
    names = [d.to_dict()["name"] for d in results]
    assert names == ["Asha"], f"Unexpected result: {names}"

    # 3. Check acme's data does not contain globex's employee
    acme_names = [d.to_dict()["name"] for d in company_employees("acme").stream()]
    assert "Mia" not in acme_names

    # 4. Clean up the test data
    for cid in ("acme", "globex"):
        for d in company_employees(cid).stream():
            d.reference.delete()

    print("All tests passed.")

if __name__ == "__main__":
    test_per_company_data()
