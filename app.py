import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firebase_admin.client()

gene_ref = db.collection("genes").document("BRCA1")
gene_ref.set({
    "symbol": "BRCA1",
    "description": "DNA repair gene"
})

phenotypes_ref = gene_ref.collection("phenotypes")

phenotypes_ref.document("HP:0003002").set({
    "name": "Breast carcinoma",
    "description": "Malignant tumor of the breast"
})

phenotypes_ref.document("HP:0100615").set({
    "name": "Ovarian carcinoma",
    "description": "Malignant tumor of the ovary"
})

print("Gene and phenotypes added successfully!");