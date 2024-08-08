import json

def read_json_and_extract_ids(json_file, output_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("JSON tidak dalam format list")

        total_ids = 0
        with open(output_file, 'w') as output_file:
            for item in data:
                if 'id' in item:
                    output_file.write(item['id'] + '\n')
                    total_ids += 1
                else:
                    print(f"Item tanpa ID: {item}")

        print(f"Total ID yang diambil: {total_ids}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

read_json_and_extract_ids('translations.json', 'output.txt')
