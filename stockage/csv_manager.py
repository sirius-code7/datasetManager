"""
datasetManager - Gestion des fichiers CSV
Partie 11 : Packages
"""

import csv
from pathlib import Path

from datasets.gestion import datasets

###############################################################################################################
# --- Partie 9.8 : Sauvegarder les datasets --- fonction 7
###############################################################################################################

def sauvegarder():

    # --- Partie 7.1 : Sauvegarde des données dans un fichier CSV ---
    with open(
        "data/datasets.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as fichier:

        colonnes = [
            "nom",
            "domaine",
            "lignes",
            "colonnes",
            "taille",
            "format",
            "public"
        ]

        writer = csv.DictWriter(
            fichier,
            fieldnames=colonnes
        )

        writer.writeheader()
        writer.writerows(datasets)

    print(
        "Les datasets ont été sauvegardés "
        "dans 'datasets.csv'.\n"
    )




###############################################################################################################
# --- Partie 9.9 : Recharger les datasets --- fonction 8
###############################################################################################################

def recharger():

    # --- Liste temporaire utilisée pour le rechargement ---
    datasets_recharges = []


    
    # --- Partie 8 : Gestion des exceptions ---

    try:

        # --- Partie 7.2 : Lecture du fichier CSV ---

        with open(
            "data/datasets.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as fichier:

            reader = csv.DictReader(fichier)
            lignes = list(reader)


            # --- Partie 8 : Vérification du fichier vide ---
            if not lignes:
                print(
                    "Le fichier 'datasets.csv' est vide "
                    "ou ne contient aucun dataset.\n"
                )

                return


            # --- Rechargement des datasets ---
            for ligne in lignes:

                dataset = {
                    "nom": ligne["nom"],
                    "domaine": ligne["domaine"],
                    "lignes": int(ligne["lignes"]),
                    "colonnes": int(ligne["colonnes"]),
                    "taille": float(ligne["taille"]),
                    "format": ligne["format"],
                    "public": ligne["public"].lower() == "true"
                }

                datasets_recharges.append(dataset)


            # --- Mise à jour de la liste principale ---
            datasets.clear()
            datasets.extend(datasets_recharges)


            print(
                "Les datasets ont été rechargés "
                "depuis 'datasets.csv'.\n"
            )


            # --- Partie 7.2 : Afficher les datasets rechargés ---

            print("===== Datasets rechargés =====")

            for dataset in datasets:

                print(
                    f"Nom        : {dataset['nom']}"
                )

                print(
                    f"Domaine    : {dataset['domaine']}"
                )

                print(
                    f"Lignes     : {dataset['lignes']}"
                )

                print(
                    f"Colonnes   : {dataset['colonnes']}"
                )

                print(
                    f"Taille     : {dataset['taille']} Mo"
                )

                print(
                    f"Format     : {dataset['format']}"
                )

                print(
                    f"Public     : "
                    f"{'Oui' if dataset['public'] else 'Non'}"
                )

                print(
                    "------------------------------"
                )

            print(
                "==============================\n"
            )


    #-----------------------------------------------------------------------------------------------------------
    # --- Partie 8 : Fichier inexistant ---
    #-----------------------------------------------------------------------------------------------------------

    except FileNotFoundError:

        print(
            "Erreur : le fichier 'datasets.csv' "
            "n'existe pas.\n"
        )


    #-----------------------------------------------------------------------------------------------------------
    # --- Partie 8 : Valeur numérique invalide ---
    #-----------------------------------------------------------------------------------------------------------

    except ValueError:

        print(
            "Erreur : une valeur numérique "
            "du fichier CSV est invalide.\n"
        )


    #-----------------------------------------------------------------------------------------------------------
    # --- Partie 8 : Colonne manquante dans le fichier ---
    #-----------------------------------------------------------------------------------------------------------

    except KeyError as erreur:

        print(
            f"Erreur : la colonne {erreur} "
            "est absente du fichier CSV.\n"
        )