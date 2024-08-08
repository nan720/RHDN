import json

# Membaca file JSON
with open('new_tools.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Misalnya, jika Anda perlu memproses data, lakukan di sini
# Contoh: hanya mencetak data
print(data)

# Menyimpan data ke file JSON baru
with open('tools_tanpa_unicode.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
