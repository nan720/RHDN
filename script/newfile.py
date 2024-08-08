import json
import re

# Data JSON
data = [{
    "url": "https://archive.org/download/romhacking.net-20240801/rhdn_20240801.zip/hacks%2Fxbox%2Fpatches%2F%5B5705%5Dngb-camera-invert-patch-v1.1.zip",
    "name": "hacks/xbox/patches/[5705]ngb-camera-invert-patch-v1.1.zip",
    "date": "2024-01-09 22:14",
    "size": "203316"
}]

# Fungsi untuk mengambil data yang diperlukan
def process_data(entry):
    name = entry["name"]
    url = entry["url"]
    
    # Mengambil angka di dalam []
    id_match = re.search(r'%5B(\d+)%5D', url)
    id_number = id_match.group(1) if id_match else ""
    
    # Mengambil text setelah %5D
    text_match = re.search(r'%5D(.*)', url)
    text_after_bracket = text_match.group(1) if text_match else ""
    
    return {
        "fName": text_after_bracket,
        "id": id_number,
        "size": entry["size"]
    }

# Proses data
processed_data = [process_data(entry) for entry in data]

# Simpan ke file JSON
with open('output.json', 'w') as file:
    json.dump(processed_data, file, indent=4)

print("Data berhasil diproses dan disimpan ke output.json")
