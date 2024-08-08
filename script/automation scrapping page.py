import requests
from bs4 import BeautifulSoup
import json

# Fungsi untuk mengunduh dan memparse halaman web
def scrape_page(page_number):
    url = f'https://www.romhacking.net/?page=translations&perpage=200&startpage={page_number}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Buat list kosong untuk menyimpan data
data_list = []

# Iterasi melalui halaman-halaman dari 2 hingga 11
for page_number in range(2, 34):
    soup = scrape_page(page_number)
    # Temukan tabel di halaman web
    tables = soup.find_all('table')
    # Iterasi melalui tabel-tabel dan ekstrak informasi yang Anda inginkan
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 8:  # Pastikan ada cukup kolom dalam baris
                title = cells[0].find('a').text.strip() if cells[0].find('a') else ''
                translator = cells[1].text.strip()
                #genre = cells[2].text.strip()
                platform = cells[3].text.strip()
                status = cells[4].text.strip()
                #version = cells[5].text.strip()
                #date = cells[6].text.strip()
                language = cells[7].text.strip()

                # Buat dictionary untuk setiap entri
                entry = {
                    "title": title,
                    "translator": translator,
                    #"genre": genre,
                    "platform": platform,
                    "status": status,
                    #"version": version,
                    #"date": date,
                    "language": language,
                    "id": cells[0].find('a')['href'] if cells[0].find('a') else ''
                }

                data_list.append(entry)

# Simpan data dalam format JSON ke dalam file
with open('translations.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

print("Hasil scraping telah disimpan dalam format JSON dalam file 'hasil_scraping.json'")
