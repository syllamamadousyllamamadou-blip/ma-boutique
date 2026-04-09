from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def lire_produits():
    # Catalogue mis à jour avec CATÉGORIES et BADGES (Style Adidas/Luxe)
    return [
        {
            "id": 1, 
            "nom": "Le Sac Classique", 
            "description": "Cuir véritable, noir absolu.",
            "prix": 45000, 
            "categorie": "Sacs",
            "badge": "NOUVEAU",
            "image": "https://images.unsplash.com/photo-1584916201218-f4242ceb4809?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 2, 
            "nom": "Collier Minimaliste", 
            "description": "Argent massif, élégance discrète.",
            "prix": 25000, 
            "categorie": "Bijoux",
            "badge": "",
            "image": "https://images.unsplash.com/photo-1599643478524-fb66f7280459?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 3, 
            "nom": "Lunettes Signature", 
            "description": "Protection UV optimale.",
            "prix": 30000, 
            "categorie": "Accessoires",
            "badge": "EXCLUSIVITÉ",
            "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        {
            "id": 4, 
            "nom": "Montre Précision", 
            "description": "Mouvement à quartz, cuir noir.",
            "prix": 85000, 
            "categorie": "Accessoires",
            "badge": "BEST-SELLER",
            "image": "https://images.unsplash.com/photo-1524592094714-0f0654ece975?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        }
    ]
