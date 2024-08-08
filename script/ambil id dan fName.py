import json
import re

# Fungsi untuk mengambil data yang diperlukan
def process_data(entry):
    name = entry["name"]
    
    # Mengambil angka di dalam []
    id_match = re.search(r'\[(\d+)\]', name)
    id_number = id_match.group(1) if id_match else ""
    
    # Mengambil text setelah ]
    text_match = re.search(r'\](.*)', name)
    text_after_bracket = text_match.group(1) if text_match else ""
    
    return {
        "fName": text_after_bracket,
        "id": id_number,
        "size": entry["size"]
    }

# Membaca data dari file
with open('hacks.json', 'r') as file:
    data = json.load(file)

# Proses data
processed_data = [process_data(entry) for entry in data]

# Simpan ke file JSON
with open('output.json', 'w') as file:
    json.dump(processed_data, file, indent=4)

print("Data berhasil diproses dan disimpan ke output.json")
