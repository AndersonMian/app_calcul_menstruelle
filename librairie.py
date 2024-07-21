import requests
from bs4 import BeautifulSoup
import streamlit as st

# Scraping des titres des articles
def scrape_titles():
    url = "https://questionsexualite.fr/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouver les titres des articles (ajustez le sélecteur CSS selon la structure du site)
    titles = []
    articles = soup('section',{'class':'RubricStratums'})
    for article in articles:
        h2 = article.find_all('RubricStratums-title heading')
        if h2:  # Vérifier si h2 existe
            title = h2.get_text(strip=True)
            titles.append(title)
        
    return titles

# Fonction principale de l'application Streamlit
def main():
    st.title("Bibliothèque des Titres d'Articles")
    st.write("Parcourir les titres des articles sur la sexualité humaine.")
    
    # Scraper les titres des articles
    titles = scrape_titles()
    
    if titles:
        st.write("## Titres des Articles")
        for i, title in enumerate(titles, start=1):
            st.write(f"{i}. {title}")
    else:
        st.write("Aucun titre trouvé. Veuillez vérifier le site ou réessayer plus tard.")

if __name__ == "__main__":
    main()
