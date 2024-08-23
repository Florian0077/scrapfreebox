# Web Scraper freebox et Téléchargeur de Fichiers

Ce script Python permet de scraper une page web, parcourir ses répertoires et télécharger tous les fichiers trouvés.

## Fonctionnalités

- Scrape récursivement une page web et ses sous-répertoires
- Télécharge tous les fichiers trouvés
- Préserve la structure des répertoires lors du téléchargement
- Évite de visiter deux fois le même lien

## Prérequis

- Python 3.x
- Bibliothèques requises : 
  - requests
  - beautifulsoup4

Vous pouvez installer les dépendances avec :
pip install requests beautifulsoup4
Copy
## Configuration

Avant d'exécuter le script, assurez-vous de modifier les variables suivantes :

- `destination_folder` : le chemin du répertoire où les fichiers seront téléchargés
- `base_url` : l'URL de la page web à scraper

## Utilisation

1. Configurez les variables mentionnées ci-dessus.
2. Exécutez le script :
python nom_du_script.py
Copy
Le script parcourra la page web, créera les sous-répertoires nécessaires et téléchargera tous les fichiers trouvés.

## Fonctionnement

1. Le script commence par scraper l'URL de base.
2. Il recherche une balise `<table>` dans la page HTML.
3. Pour chaque lien trouvé dans la table :
   - Si c'est un répertoire, il est scrapé récursivement.
   - Si c'est un fichier, il est téléchargé.
4. Les fichiers sont sauvegardés dans le répertoire de destination, en préservant la structure des dossiers.

## Avertissement

Assurez-vous d'avoir la permission de télécharger le contenu du site web que vous scrapez.
