import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote


# Répertoire de destination sur votre ordinateur
destination_folder = "repertoire_de_destination"
# URL de la page web à scraper
base_url = "url_de_la_freebox"
url = base_url


# Fonction pour télécharger un fichier depuis une URL
def download_file(url, destination_folder):
    # Récupérer le nom du fichier à partir de l'URL
    file_name = os.path.basename(unquote(urlparse(url).path))
    # Chemin complet de destination du fichier sur votre ordinateur
    file_path = os.path.join(destination_folder, file_name)

    # Télécharger le fichier
    with open(file_path, "wb") as file:
        response = requests.get(url)
        file.write(response.content)

    print(f"Le fichier {file_name} a été téléchargé avec succès.")


# Fonction récursive pour scraper les liens de fichiers à l'intérieur de la balise <table>
def scrape_files_in_table(url, destination_folder, visited_links=set()):
    # Ajouter l'URL actuelle aux liens visités
    visited_links.add(url)

    # Obtenir le contenu de la page web
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver la balise <table>
    table = soup.find("table")
    if table:
        # Parcourir tous les liens dans la balise <table>
        for link in table.find_all("a"):
            href = link.get("href")
            if href:
                # Construire l'URL complète
                full_url = urljoin(url, href)

                # Si le lien n'a pas déjà été visité
                if full_url not in visited_links:
                    # Si le lien est un répertoire, scraper récursivement
                    if full_url.endswith("/"):
                        subdir_name = unquote(
                            os.path.basename(urlparse(full_url).path[:-1])
                        )  # Décoder les caractères d'échappement URL
                        subdir_path = os.path.join(destination_folder, subdir_name)
                        os.makedirs(subdir_path, exist_ok=True)
                        scrape_files_in_table(full_url, subdir_path, visited_links)
                    # Sinon, si le lien est un fichier, le télécharger
                    else:
                        download_file(full_url, destination_folder)


# Appeler la fonction principale pour commencer le scraping
scrape_files_in_table(url, destination_folder)
