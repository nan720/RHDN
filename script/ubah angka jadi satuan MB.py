import json
import os

# Fungsi untuk mengkonversi ukuran dari byte ke format yang lebih mudah dibaca
def convert_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"
    elif size_in_bytes < 1048576:  # 1024**2
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1073741824:  # 1024**3
        return f"{size_in_bytes / 1048576:.2f} MB"
    else:
        return f"{size_in_bytes / 1073741824:.2f} GB"

# Path folder yang berisi file JSON
folder_path = 'kategori'

# Iterasi melalui semua file dalam folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        # Membaca file JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Memproses setiap item dalam data
        for item in data:
            if 'size' in item:
                try:
                    size_in_bytes = int(item['size'])  # pastikan size adalah integer
                    item['size'] = convert_size(size_in_bytes)
                except ValueError:
                    # Jika item['size'] bukan angka, lewati
                    continue
        
        # Menyimpan file JSON yang telah diperbarui sebagai file baru
        new_file_path = os.path.join(folder_path, f"{filename}")
        with open(new_file_path, 'w') as file:
            json.dump(data, file, indent=4)
