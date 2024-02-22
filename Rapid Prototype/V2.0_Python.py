import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Wirft eine Ausnahme im Fehlerfall
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")
        return None

def parse_html(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    return None

# Nutzereingabe für die URL
url = input("Gib die URL ein: ")

# Aufruf der Funktionen
html_content = get_html(url)

if html_content:
    dom = parse_html(html_content)
    print("DOM erfolgreich geladen.")
else:
    print("Fehler beim Laden des DOMs.")


# Beginn der Test-Funktionen

## Alt-Tags
# Finde alle img-Tags ohne Alt-Text 
imgs_without_alt = dom.find_all('img', alt=None)

# Gibt eine Warnung aus, wenn Bilder ohne Alt-Text gefunden wurden
if imgs_without_alt:
    print("Warnung: Folgende Bilder haben keinen Alt-Text:")
    for img_tag in imgs_without_alt:
        src = img_tag.get('src')
        print(f"Quell-URL: {src}")
else:
    print("Alle Bilder haben einen Alt-Text.")
