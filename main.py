"""
datasetManager - Application console de gestion de jeux de données
--------------------------------------------------------------------
Partie 1 : Types de base, variables, Entrées / Sorties
Partie 2 : Structures de contrôle
Partie 3 : Dictionnaires
Partie 4 : Tuples
------------------------------------------------
Partie 5 : Listes (5.1 - Ajouter un dataset)
Partie 5 : Listes (5.2 - Trier les datasets)
Partie 5 : Listes (5.3 - Rechercher un dataset)
Partie 5 : Listes (5.4 - Modifier un dataset)
Partie 5 : Listes (5.5 - Supprimer un dataset)
------------------------------------------------
Partie 6 : Statistiques
---------------------------------------------------------------------
Partie 7.1 : Sauvegarde les données dans un fichier CSV
Partie 7.2 : Recharger + afficher les données depuis un fichier CSV
---------------------------------------------------------------------
Partie 8 : Les exceptions
---------------------------------------------------------------------
Partie 9 : Fonctions
---------------------------------------------------------------------
Partie 10 : Modules
"""

import csv

from menu import afficher_menu
from cs50 import get_string, get_int, get_float
from gestion import DOMAINES_AUTORISES, datasets


###############################################################################################################
# --- Partie 9.2 : Ajouter un dataset --- fonction 1
###############################################################################################################

def ajouter_dataset():

    # --- Saisie des métadonnées du dataset ---
    nom = get_string("Nom du dataset : ")

    domaine = get_string(
        f"Domaine {DOMAINES_AUTORISES} : "
    )

    while domaine not in DOMAINES_AUTORISES:
        print(
            "Domaine invalide, choisissez parmi la liste proposée.\n"
        )

        domaine = get_string(
            f"Domaine {DOMAINES_AUTORISES} : "
        )

    lignes = get_int("Nombre de lignes : ")
    colonnes = get_int("Nombre de colonnes : ")
    taille = get_float("Taille en Mo : ")
    format_fichier = get_string(
        "Format (csv ou json) : "
    )

    public = (
        get_string(
            "Public ? (true/false) : "
        )
        .strip()
        .lower()
        == "true"
    )

#*************************************************************************************************************    # --- Partie 3 : Stockage dans un dictionnaire ---
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

#*************************************************************************************************************    # --- Partie 5.1 : Ajout du dataset dans la liste ---
    # --- Partie 5.1 : Ajout du dataset dans la liste ---
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
    print(
        f"Dataset '{dataset['nom']}' ajouté avec succès.\n"
    )


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


###############################################################################################################
# --- Partie 9.4 : Supprimer un dataset --- fonction 3
###############################################################################################################

def supprimer_dataset():

    # --- Vérification de la présence de datasets ---
    if not datasets:
        print("Aucun dataset disponible pour la suppression.\n")

    else:
        nom_suppression = get_string(
            "Nom du dataset à supprimer : "
        )

        dataset_trouve = None


        # --- Partie 5.5 : Recherche du dataset à supprimer ---
        for dataset in datasets:
            if (
                dataset["nom"].lower()
                == nom_suppression.lower()
            ):
                dataset_trouve = dataset
                break


        # --- Suppression du dataset trouvé ---
        if dataset_trouve is None:
            print(
                f"Dataset '{nom_suppression}' non trouvé.\n"
            )

        else:
            datasets.remove(
                dataset_trouve
            )

            print(
                f"Le dataset '{nom_suppression}' "
                "a été supprimé avec succès.\n"
            )

###############################################################################################################
# --- Partie 9.5 : Rechercher un dataset --- fonction 4
###############################################################################################################

def rechercher_dataset():

    # --- Vérifier si le datasets est là ---
    if not datasets:
        print(
            "Aucun dataset disponible pour la recherche.\n"
        )

    else:
        nom_recherche = get_string(
            "Nom du dataset à rechercher : "
        )

        dataset_trouve = None


        # --- Partie 5.3 : Recherche du dataset ---
        for dataset in datasets:
            if (
                dataset["nom"].lower()
                == nom_recherche.lower()
            ):
                dataset_trouve = dataset
                break


        # --- Affichage du résultat de la recherche ---
        if dataset_trouve is None:
            print(
                f"Dataset '{nom_recherche}' non trouvé.\n"
            )

        else:
            print(
                "\n===== Résultat de la recherche ====="
            )
            print(
                f"Nom        : {dataset_trouve['nom']}"
            )
            print(
                f"Domaine    : {dataset_trouve['domaine']}"
            )
            print(
                f"Lignes     : {dataset_trouve['lignes']}"
            )
            print(
                f"Colonnes   : {dataset_trouve['colonnes']}"
            )
            print(
                f"Taille     : {dataset_trouve['taille']} Mo"
            )
            print(
                f"Format     : {dataset_trouve['format']}"
            )
            print(
                f"Public     : "
                f"{'Oui' if dataset_trouve['public'] else 'Non'}"
            )
            print(
                "====================================\n"
            )

###############################################################################################################
# --- Partie 9.6 : Trier les datasets --- fonction 5
###############################################################################################################

def trier_dataset():

    # --- Vérification de la présence de datasets ---
    if not datasets:
        print(
            "Aucun dataset disponible pour le tri.\n"
        )

    else:

        # --- Partie 5.2 : Tri des datasets par nom ---
        datasets.sort(
            key=lambda dataset: dataset["nom"].lower()
        )

        print(
            "\n===== Datasets triés par nom ====="
        )

        for dataset in datasets:
            print(
                f"- {dataset['nom']}"
            )

        print(
            "==================================\n"
        )

###############################################################################################################
# --- Partie 9.7 : Modifier un dataset --- fonction 6
###############################################################################################################

def modifier_dataset():

    # --- Vérification de la présence de datasets ---
    if not datasets:
        print(
            "Aucun dataset disponible pour la modification.\n"
        )

    else:
        nom_modification = get_string(
            "Nom du dataset à modifier : "
        )

        dataset_trouve = None


        # --- Partie 5.4 : Recherche du dataset à modifier ---
        for dataset in datasets:
            if (
                dataset["nom"].lower()
                == nom_modification.lower()
            ):
                dataset_trouve = dataset
                break


        # --- Verifier si le dataset existe ---
        if dataset_trouve is None:
            print(
                f"Dataset '{nom_modification}' non trouvé.\n"
            )

        else:
            print(
                f"\nModification du dataset "
                f"'{dataset_trouve['nom']}'"
            )


            # --- Saisie des nouvelles métadonnées ---
            nouveau_nom = get_string(
                "Nouveau nom du dataset : "
            )

            nouveau_domaine = get_string(
                f"Nouveau domaine {DOMAINES_AUTORISES} : "
            )

            while nouveau_domaine not in DOMAINES_AUTORISES:
                print(
                    "Domaine invalide, choisissez parmi "
                    "la liste proposée.\n"
                )

                nouveau_domaine = get_string(
                    f"Nouveau domaine {DOMAINES_AUTORISES} : "
                )

            nouvelles_lignes = get_int(
                "Nouveau nombre de lignes : "
            )

            nouvelles_colonnes = get_int(
                "Nouveau nombre de colonnes : "
            )

            nouvelle_taille = get_float(
                "Nouvelle taille en Mo : "
            )

            nouveau_format = get_string(
                "Nouveau format (csv ou json) : "
            )

            nouveau_public = (
                get_string(
                    "Le dataset est-il public ? "
                    "(true/false) : "
                )
                .strip()
                .lower()
                == "true"
            )


            # --- Partie 5.4 : Mise à jour des métadonnées ---
            dataset_trouve["nom"] = nouveau_nom
            dataset_trouve["domaine"] = nouveau_domaine
            dataset_trouve["lignes"] = nouvelles_lignes
            dataset_trouve["colonnes"] = nouvelles_colonnes
            dataset_trouve["taille"] = nouvelle_taille
            dataset_trouve["format"] = nouveau_format.upper()
            dataset_trouve["public"] = nouveau_public


            print(
                f"\nLe dataset '{nom_modification}' "
                "a été modifié avec succès.\n"
            )

###############################################################################################################
# --- Partie 9.8 : Sauvegarder les datasets --- fonction 7
###############################################################################################################

def sauvegarder():

    # --- Partie 7.1 : Sauvegarde des données dans un fichier CSV ---
    with open(
        "datasets.csv",
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
            "datasets.csv",
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

###############################################################################################################
# --- Partie 9.10 : Afficher les statistiques ---
###############################################################################################################

def statistiques():

    # --- Vérification de la présence de datasets ---
    if not datasets:
        print(
            "Aucun dataset disponible "
            "pour afficher les statistiques.\n"
        )

    else:

        #------------------------------------------------------------------------------------------------------
        # --- Partie 6 : Compréhensions de listes ---
        #------------------------------------------------------------------------------------------------------

        datasets_publics = [
            dataset
            for dataset in datasets
            if dataset["public"]
        ]

        datasets_prives = [
            dataset
            for dataset in datasets
            if not dataset["public"]
        ]

        datasets_csv = [
            dataset
            for dataset in datasets
            if dataset["format"] == "CSV"
        ]

        datasets_json = [
            dataset
            for dataset in datasets
            if dataset["format"] == "JSON"
        ]

        lignes_datasets = [
            dataset["lignes"]
            for dataset in datasets
        ]

        colonnes_datasets = [
            dataset["colonnes"]
            for dataset in datasets
        ]


        #------------------------------------------------------------------------------------------------------
        # --- Partie 6 : Compréhension de dictionnaire ---
        #------------------------------------------------------------------------------------------------------

        repartition_domaines = {
            domaine: sum(
                1
                for dataset in datasets
                if dataset["domaine"] == domaine
            )
            for domaine in DOMAINES_AUTORISES
        }


        #------------------------------------------------------------------------------------------------------
        # --- Calcul des statistiques ---
        #------------------------------------------------------------------------------------------------------

        nombre_datasets = len(datasets)

        total_lignes = sum(
            lignes_datasets
        )

        moyenne_colonnes = (
            sum(colonnes_datasets)
            / nombre_datasets
        )


        #------------------------------------------------------------------------------------------------------
        # --- Affichage des statistiques ---
        #------------------------------------------------------------------------------------------------------

        print(
            "\n===== Statistiques des datasets ====="
        )

        print(
            f"Nombre de datasets       : "
            f"{nombre_datasets}"
        )

        print(
            f"Nombre total de lignes   : "
            f"{total_lignes}"
        )

        print(
            f"Nombre moyen de colonnes : "
            f"{moyenne_colonnes:.2f}"
        )

        print(
            f"Datasets publics         : "
            f"{len(datasets_publics)}"
        )

        print(
            f"Datasets privés          : "
            f"{len(datasets_prives)}"
        )

        print(
            f"Datasets au format CSV   : "
            f"{len(datasets_csv)}"
        )

        print(
            f"Datasets au format JSON  : "
            f"{len(datasets_json)}"
        )


        print(
            "\nRépartition par domaine :"
        )

        for domaine, nombre in repartition_domaines.items():
            print(
                f"- {domaine} : {nombre}"
            )

        print(
            "======================================\n"
        )

#*************************************************************************************************************    # --- Partie 2 : Menu interactif ---
# --- Partie 2 : Menu interactif (provisoire) --- fonction 0
while True:
    choix = afficher_menu()

#*************************************************************************************************************     # --- Partie 5.1 : Ajouter un dataset ---
    # --- Partie 5.1 : Ajouter un dataset --- fonction 1
    if choix == 1:
        ajouter_dataset()

#*************************************************************************************************************     # --- Partie 5.1 : Ajouter un dataset ---
    # ---  Affichage de tous les datasets  --- fonction 2
    elif choix == 2:
        afficher_datasets()

#*************************************************************************************************************     # --- Partie 5.2 : Trier les datasets  ---

    # --- Partie 5.2 : Trier les datasets  --- fonction 5
    elif choix == 3:
        trier_dataset()

#*************************************************************************************************************     # --- Partie 5.3 : Rechercher un dataset  ---

    # --- Partie 5.3 : Rechercher un dataset  --- fonction 4
    elif choix == 4:
        rechercher_dataset()

#*************************************************************************************************************     # --- Partie 5.4 : Modifier un dataset  ---

    # --- Partie 5.4 : Modifier un dataset  --- fonction 6
    elif choix == 5:
        modifier_dataset()  

#*************************************************************************************************************    # --- Partie 5.5 : Supprimer un dataset  ---

    # --- Partie 5.5 : Supprimer un dataset  --- Fonction 3
    elif choix == 6:
        supprimer_dataset()

#*************************************************************************************************************     # --- Partie 6 : Statistiques ---

    # --- Partie 6 : Statistiques --- fonction 9
    elif choix == 7:
        statistiques()

#*************************************************************************************************************       # --- Partie 7.1 : Sauvegarder les données dans un fichier CSV ---

        # --- Partie 7.1 : Sauvegarder les données dans un fichier CSV --- fonction 7

    elif choix == 8:
        sauvegarder()

#*************************************************************************************************************     # --- Partie 7.2 : Recharger + afficher les données depuis un fichier CSV ---

    # --- Partie 7.2 : Recharger + afficher les données depuis un fichier CSV --- fonction 8

    elif choix == 9:
        recharger()

#*************************************************************************************************************     # --- Quitter l'application ---

    elif choix == 10:
        print("Au revoir !")
        break

    else:
        print("Choix invalide, veuillez réessayer.\n")