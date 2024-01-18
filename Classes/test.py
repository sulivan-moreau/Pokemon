import pandas as pd

# Chemin du fichier CSV
fichier_csv = 'Ressource/BDD.csv'  # Assurez-vous que le chemin est correct

# Essayer différents encodages
encodings = ['latin1', 'ISO-8859-1', 'cp1252']
for encoding in encodings:
    try:
        df = pd.read_csv(fichier_csv, sep=';', encoding=encoding)
        print(f"Chargé avec succès en utilisant l'encodage {encoding}")
        print(df.head())  # Afficher les premières lignes pour vérifier
        break
    except UnicodeDecodeError as e:
        print(f"Erreur avec l'encodage {encoding}: {e}")

# Si le DataFrame n'est pas chargé, signaler l'erreur
if 'df' not in locals():
    print("Échec du chargement du fichier avec les encodages testés.")
