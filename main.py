"""
datasetManager - Application console de gestion de jeux de données
Partie 1 : Types de base, variables, Entrées / Sorties
"""

from cs50 import get_string, get_int, get_float

# --- Saisie des métadonnées du dataset ---

nom = get_string("Nom du dataset : ")
domaine = get_string("Domaine (Santé, Finance, Agriculture, Transport, Education ...) : ")
lignes = get_int("Nombre de lignes : ")
colonnes = get_int("Nombre de colonnes : ")
taille = get_float("Taille en Mo : ")
format_fichier = get_string("Format (csv ou json) : ")
public = get_string("Public ? (true/false) : ").strip().lower() == "true"

# --- Affichage du résumé formaté ---

print("\n===== Résumé du dataset =====")
print(f"Nom        : {nom}")
print(f"Domaine    : {domaine}")
print(f"Lignes     : {lignes}")
print(f"Colonnes   : {colonnes}")
print(f"Taille     : {taille} Mo")
print(f"Format     : {format_fichier.upper()}")
print(f"Public     : {'Oui' if public else 'Non'}")
print("==============================\n")