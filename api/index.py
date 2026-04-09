from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autorise la vitrine web (index.html) à communiquer avec cette API Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def lire_produits():
    # Catalogue officiel de Maison Sylla
    # Les catégories (Homme, Femme, Enfants) doivent correspondre exactement aux boutons du site
    return [
        {
            "id": 1, 
            "nom": "Ensemble Coton Premium", 
            "description": "Confort absolu, coupe moderne pour homme. Idéal pour le quotidien ou les occasions décontractées.",
            "prix": 45000, 
            "categorie": "Homme",
            "badge": "NOUVEAU",
            "image": "https://images.unsplash.com/photo-1617137968427-85924c800a22?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 2, 
            "nom": "Robe de Soirée Élégante", 
            "description": "Design exclusif, parfaite pour vos événements. Finitions soignées et tissu premium.",
            "prix": 65000, 
            "categorie": "Femme",
            "badge": "EXCLUSIVITÉ",
            "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 3, 
            "nom": "Baskets Urbaines", 
            "description": "Style streetwear, robustes et confortables. Conçues pour durer.",
            "prix": 35000, 
            "categorie": "Homme",
            "badge": "",
            "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 4, 
            "nom": "T-shirt Coton Enfant", 
            "description": "Doux pour la peau, résistant aux jeux. Lavage facile en machine.",
            "prix": 15000, 
            "categorie": "Enfants",
            "badge": "BEST-SELLER",
            "image": "https://images.unsplash.com/photo-1519241047957-be31d7379a5d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        }
    ]
