from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import csv
import urllib.request
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⚠️ TON ID GOOGLE SHEET
SHEET_ID = "1JKuBcj5vSInz0pp7vwKSDyuW-4Lu763SZRFngUSdcs0" 
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

@app.get("/api")
def lire_produits():
    try:
        response = urllib.request.urlopen(SHEET_URL)
        csv_data = response.read().decode('utf-8')
        
        lecteur = csv.DictReader(io.StringIO(csv_data))
        produits = []
        
        for ligne in lecteur:
            if not ligne.get('nom') or not ligne['nom'].strip(): 
                continue
                
            produit = {
                "id": int(ligne['id']) if ligne.get('id') else 0,
                "nom": ligne['nom'],
                "description": ligne['description'],
                "prix": int(ligne['prix']) if ligne.get('prix') else 0,
                "ancien_prix": int(ligne['ancien_prix']) if ligne.get('ancien_prix') else None,
                "stock": int(ligne['stock']) if ligne.get('stock') else 0,
                # Sécurisation de la catégorie (nettoie les espaces)
                "categorie": str(ligne.get('categorie', 'Divers')).strip() or 'Divers',
                "badge": ligne.get('badge', ""),
                "image": ligne['image']
            }
            produits.append(produit)
            
        return produits

    except Exception as e:
        print(f"Erreur lors de la lecture du Google Sheet : {e}")
        return []
