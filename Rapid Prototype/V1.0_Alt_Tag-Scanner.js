const axios = require('axios');
const cheerio = require('cheerio');

// Funktion zum Abrufen des HTML-Codes einer Webseite durch Acios HTTP-Client
async function getHtml(url) {
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error('Fehler beim Abrufen der Webseite:', error.message);
        return null;
    }
}

// Funktion zum Extrahieren der Alt-Texte aus dem HTML-Code mit Cheerio
function extractAltTexts(htmlCode) {
    const webpage = cheerio.load(htmlCode);
    const imgTags = webpage('img');

        if (imgTags.length > 0) {
            imgTags.each((index, element) => {
                const altText = webpage(element).attr('alt');
                if (altText) {
                    console.log(`Bild ${index + 1} hat Alt-Tag: ${altText}`);
                } else {
                    console.log(`Bild ${index + 1} hat keinen Alt-Tag.`);
                }
            });
        } else {
            console.log('Keine Bilder gefunden.');
        }
    }

// URL der Webseite, deren HTML analysiert werden soll
const websiteUrl = 'https://www.kinopolis.de/ko';

// HTML-Code der Webseite abrufen
getHtml(websiteUrl).then(htmlCode => {
    if (htmlCode) {
        // Alt-Tags aus dem HTML-Code extrahieren und ausgeben
        extractAltTexts(htmlCode);
    }
});