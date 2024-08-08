import json

# Membaca file results.json
try:
    with open('output.json', 'r') as results_file:
        results_data = json.load(results_file)
except FileNotFoundError:
    print("File results.json tidak ditemukan.")
    exit()
except json.JSONDecodeError:
    print("Format file results.json tidak valid.")
    exit()

# Membaca file translations.json
try:
    with open('hacks.json', 'r') as translations_file:
        translations_data = json.load(translations_file)
except FileNotFoundError:
    print("File translations.json tidak ditemukan.")
    exit()
except json.JSONDecodeError:
    print("Format file translations.json tidak valid.")
    exit()

# Membuat dictionary dari results.json untuk pencocokan cepat
results_dict = {}
for item in results_data:
    if 'id' in item and 'img' in item:
        results_dict[item['id']] = item['img']
    else:
        print(f"Item dengan id {item.get('id', 'unknown')} tidak memiliki key 'img'.")

# Menambahkan "img" ke translations.json jika "id" cocok
for translation in translations_data:
    if 'id' in translation and translation['id'] in results_dict:
        translation['img'] = results_dict[translation['id']]

# Menyimpan perubahan ke file translations.json
try:
    with open('hacks_new.json', 'w') as translations_file:
        json.dump(translations_data, translations_file, indent=4)
    print("File translations.json telah diperbarui.")
except IOError:
    print("Gagal menyimpan file translations.json.")
