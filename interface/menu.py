from cs50 import get_int


#*************************************************************************************************************
# --- Partie 10 : Menu ---

def afficher_menu():
    print("\n")
    print("========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Trier les datasets")
    print("4. Rechercher un dataset")
    print("5. Modifier un dataset")
    print("6. Supprimer un dataset")
    print("7. Afficher les statistiques")
    print("8. Sauvegarder les datasets")
    print("9. Recharger les datasets")
    print("10. Quitter")
    print("========================")

    return get_int("Votre choix : ")