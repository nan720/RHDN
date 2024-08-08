import json

# Membaca hacks.json
with open('hacks.json', 'r') as file:
    hacks_data = json.load(file)

# Membaca output.json
with open('output.json', 'r') as file:
    output_data = json.load(file)

# Membuat dictionary untuk output_data berdasarkan id
output_dict = {item['id']: item for item in output_data}

# Menggabungkan data
for entry in hacks_data:
    entry_id = entry.get('id')
    if entry_id in output_dict:
        output_entry = output_dict[entry_id]
        entry['fName'] = output_entry['fName']
        entry['size'] = output_entry['size']

# Menyimpan hasil ke hacks.json
with open('hacks.json', 'w') as file:
    json.dump(hacks_data, file, indent=4)

print("Data berhasil digabungkan dan disimpan ke hacks.json")
