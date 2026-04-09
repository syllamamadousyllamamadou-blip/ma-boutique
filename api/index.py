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

# ⚠️ REMPLACE CETTE VALEUR PAR L'ID DE TON GOOGLE SHEET
SHEET_ID = "1JKuBcj5vSInz0pp7vwKSDyuW-4Lu763SZRFngUSdcs0" 
# Ne touche pas à cette ligne, elle transforme ton Sheet en fichier CSV lisible par Python
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

@app.get("/api")
def lire_produits():
    try:
        # 1. Python va télécharger ton Google Sheet
        response = urllib.request.urlopen(SHEET_URL)
        csv_data = response.read().decode('utf-8')
        
        # 2. Il lit les lignes
        lecteur = csv.DictReader(io.StringIO(csv_data))
        produits = []
        
        for ligne in lecteur:
            # Sécurité : on ignore les lignes vides
            if not ligne['nom']: continue
                
            # On formate les données pour que le site web les comprenne bien
            produit = {
                "id": int(ligne['id']) if ligne['id'] else 0,
                "nom": ligne['nom'],
                "description": ligne['description'],
                "prix": int(ligne['prix']) if ligne['prix'] else 0,
                "ancien_prix": int(ligne['ancien_prix']) if ligne.get('ancien_prix') else None,
                "stock": int(ligne['stock']) if ligne.get('stock') else 0,
                "categorie": ligne['categorie'],
                "badge": ligne.get('badge', ""),
                "image": ligne['image']
            }
            produits.append(produit)
            
        return produits

    except Exception as e:
        # En cas d'erreur (problème de lien, etc.), on renvoie une liste vide
        print(f"Erreur lors de la lecture du Google Sheet : {e}")
        return []
