

from datasets.gestion import datasets, DOMAINES_AUTORISES

###############################################################################################################
# --- Partie 9.3 : Afficher les datasets --- fonction 2
###############################################################################################################

def afficher_datasets():

    # --- Vérification de la présence de datasets ---
    if not datasets:
        print("Aucun dataset disponible.\n")

    else:
        print("\n===== Liste des datasets =====")

        for dataset in datasets:
            print(f"Nom        : {dataset['nom']}")
            print(f"Domaine    : {dataset['domaine']}")
            print(f"Lignes     : {dataset['lignes']}")
            print(f"Colonnes   : {dataset['colonnes']}")
            print(f"Taille     : {dataset['taille']} Mo")
            print(f"Format     : {dataset['format']}")
            print(f"Public     : {'Oui' if dataset['public'] else 'Non'}")
            print("------------------------------")

        print("==============================\n")