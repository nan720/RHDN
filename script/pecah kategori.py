import json

# Membaca data dari file JSON
with open('rhdn.json', 'r') as json_file:
    data = json.load(json_file)

# Dictionary untuk menyimpan data terpisah
categorized_data = {}

# Memisahkan data berdasarkan kategori
for item in data:
    category = item['name'].split('/')[0]
    if category not in categorized_data:
        categorized_data[category] = []
    categorized_data[category].append(item)

# Menyimpan data terpisah ke file JSON
for category, items in categorized_data.items():
    file_name = f"{category}.json"
    with open(file_name, 'w') as json_file:
        json.dump(items, json_file, indent=4)

print("Data telah dipisahkan dan disimpan ke file JSON terpisah.")
