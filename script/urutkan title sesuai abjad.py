import json
import os

# Nama folder yang berisi file JSON
folder_path = 'api'

# Mengambil daftar semua file JSON dalam folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        # Membaca file JSON
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Menyortir data berdasarkan kunci 'title'
        sorted_data = sorted(data, key=lambda x: x['title'])
        
        # Menyimpan data yang sudah diurutkan ke file baru
        new_filename = f'new_{filename}'
        new_file_path = os.path.join(folder_path, new_filename)
        with open(new_file_path, 'w') as file:
            json.dump(sorted_data, file, indent=2)

        print(f"File {filename} telah diurutkan dan disimpan sebagai {new_filename}.")
