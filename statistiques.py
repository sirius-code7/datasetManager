
from gestion import datasets, DOMAINES_AUTORISES


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