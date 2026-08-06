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

from menu import afficher_menu

from gestion import (
    ajouter_dataset,
    afficher_datasets,
    supprimer_dataset,
    rechercher_dataset,
    trier_dataset,
    modifier_dataset,
    sauvegarder,
    recharger
)

from statistiques import statistiques

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