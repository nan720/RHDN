from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder="html", static_folder="static")

# Atribut Tambahan  
app.url_map.strict_slashes = False

# Data JSON untuk rute otomatis
data_json = {
    "translations": {
        "title": "Translations",
        "url": "http://127.0.0.1:5000/static/translations.json"
    },
    "tools": {
        "title": "tools",
        "url": "http://127.0.0.1:5000/static/tools.json"
    },
    "a": {
        "title": "a",
        "url": "http://127.0.0.1:5000/static/hacks.json"
    },
    # Tambahkan data lainnya seperti di atas
}

# Rute Otomatis berdasarkan data JSON
@app.route('/<page_name>', methods=['GET', 'POST'])
def show_page(page_name):
    # Mengalihkan ke halaman 404 jika path roms yang dituju tidak tersedia pada syntax JSON
    if page_name not in data_json:
        return render_template('error_page/404.html')
    
    title = data_json[page_name]['title']
    url = data_json[page_name]['url']
    path = page_name
    
    # Mengambil data dari API
    data = requests.get(url).json()
    
    # Memastikan data memiliki struktur yang konsisten
    if isinstance(data, list):
        items = data  # Jika data sudah dalam bentuk list
    elif isinstance(data, dict) and 'results' in data:
        items = data['results']  # Jika data adalah dict dan ada key 'results'
    else:
        items = []  # Jika strukturnya tidak dikenal, buat items kosong
    
    return render_template('dl.html', title=title, items=items, path=path)

# Rute untuk menampilkan halaman berdasarkan ID
@app.route('/<page_name>/<id>', methods=['GET', 'POST'])
def download_link(page_name, id):
    # Cek apakah url sudah benar
    if page_name not in data_json:
        return render_template('error_page/404.html')
    
    # Mengambil data dari API
    url_api = data_json[page_name]['url']
    path = data_json[page_name]['title']
    data_links = requests.get(url_api).json().get('results', [])
    
    # Mencari link yang sesuai dengan id yang diberikan
    for data_link in data_links:
        if data_link.get('id') == id:
            url_file = data_link.get('fName')
            name_file = data_link.get('title')
            size = data_link.get('size')
            translator = data_link.get('translator', 'N/A')
            return render_template('redirect.html', name_file=name_file, url_file=url_file, path=path, size=size, translator=translator)
    
    # Jika link tidak ditemukan, kirimkan pesan error
    return redirect(url_for('index'))

# Index route
@app.route('/', methods=['GET', 'POST'])
def index():
    tRoms = "27.357"
    return render_template('konsol.html', tRoms=tRoms)

# Jalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
