import requests
from bs4 import BeautifulSoup
import json

# Unduh halaman web
url = 'https://www.romhacking.net/?page=translations&status=&platform=&languageid=&order=Date&perpage=200&dir=0&title=&transsearch=Go'
response = requests.get(url)

# Parse halaman web menggunakan BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Temukan tabel di halaman web
tables = soup.find_all('table')

# Buat list kosong untuk menyimpan data
data_list = []

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
                "url": cells[0].find('a')['href'] if cells[0].find('a') else ''
            }

            data_list.append(entry)

# Simpan data dalam format JSON ke dalam file
with open('hasil_scraping.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

print("Hasil scraping telah disimpan dalam format JSON dalam file 'hasil_scraping.json'")
