"""
datasetManager - Application console de gestion de jeux de données
Partie 1 : Types de base, variables, Entrées / Sorties
Partie 2 : Structures de contrôle
Partie 3 : Dictionnaires
Partie 4 : Tuples
Partie 5 : Listes (5.1 - Ajouter un dataset)
"""

from cs50 import get_string, get_int, get_float

# --- Partie 4 : Domaines autorisés (immuables) ---
DOMAINES_AUTORISES = ("Santé", "Finance", "Agriculture", "Transport", "Education")

# --- Partie 5 : Liste contenant les datasets ---
datasets = []

# --- Partie 2 : Menu interactif (provisoire) ---
while True:
    print("========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    print("========================")

    choix = get_int("Votre choix : ")

    if choix == 1:
        # --- Saisie des métadonnées du dataset ---
        nom = get_string("Nom du dataset : ")

        domaine = get_string(f"Domaine {DOMAINES_AUTORISES} : ")
        while domaine not in DOMAINES_AUTORISES:
            print("Domaine invalide, choisissez parmi la liste proposée.\n")
            domaine = get_string(f"Domaine {DOMAINES_AUTORISES} : ")

        lignes = get_int("Nombre de lignes : ")
        colonnes = get_int("Nombre de colonnes : ")
        taille = get_float("Taille en Mo : ")
        format_fichier = get_string("Format (csv ou json) : ")
        public = get_string("Public ? (true/false) : ").strip().lower() == "true"

        # --- Partie 3 : Stockage dans un dictionnaire ---
        dataset = {
            "nom": nom,
            "domaine": domaine,
            "lignes": lignes,
            "colonnes": colonnes,
            "taille": taille,
            "format": format_fichier.upper(),
            "public": public
        }

        # --- Partie 5 : Ajout du dataset dans la liste ---
        datasets.append(dataset)

        # --- Affichage du résumé formaté du dataset ajouté ---
        print("\n===== Résumé du dataset =====")
        print(f"Nom        : {dataset['nom']}")
        print(f"Domaine    : {dataset['domaine']}")
        print(f"Lignes     : {dataset['lignes']}")
        print(f"Colonnes   : {dataset['colonnes']}")
        print(f"Taille     : {dataset['taille']} Mo")
        print(f"Format     : {dataset['format']}")
        print(f"Public     : {'Oui' if dataset['public'] else 'Non'}")
        print("==============================")
        print(f"Dataset '{dataset['nom']}' ajouté avec succès.\n")

    elif choix == 2:
        print("→ (à venir) Afficher les datasets\n")

    elif choix == 3:
        print("→ (à venir) Rechercher un dataset\n")

    elif choix == 4:
        print("Au revoir !")
        break

    else:
        print("Choix invalide, veuillez réessayer.\n")