import json

# Baca data dari file JSON
with open('fileB_modified.json', 'r') as file:
    data = json.load(file)

# Filter data yang memiliki fName
filtered_data = [item for item in data if 'fName' in item]

# Tulis data yang sudah difilter kembali ke file JSON
with open('filtered_data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)

print("Data yang memiliki 'fName' telah disimpan ke 'filtered_data.json'.")