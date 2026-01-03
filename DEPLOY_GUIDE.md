# Deploy Django ke PythonAnywhere

## Langkah-langkah:

### 1. Upload Project
- Zip semua file project
- Upload ke PythonAnywhere via Files tab
- Extract di `/home/akbrln/`

### 2. Install Dependencies
Buka Bash console di PythonAnywhere:
```bash
cd Laporan-Magang
pip3.10 install --user -r requirements.txt
```

### 3. Setup Database
```bash
python3.10 manage.py migrate
python3.10 manage.py collectstatic
python3.10 manage.py createsuperuser
```

### 4. Web App Configuration
- Go to Web tab
- Create new web app
- Choose Manual configuration
- Python version: 3.10
- Source code: `/home/akbrln/laporan_magang`
- WSGI file: copy content dari `wsgi_pythonanywhere.py`

### 5. Static Files
Di Web tab, tambahkan:
- URL: `/static/`
- Directory: `/home/akbrln/laporan_magang/static/`
- URL: `/media/`
- Directory: `/home/akbrln/laporan_magang/media/`

### 6. Update Settings
Edit `config/production_settings.py`:
- Ganti `yourusername` dengan username PythonAnywhere kamu
- Set `ALLOWED_HOSTS = ['akbrln.pythonanywhere.com']`

### 7. Reload Web App
Klik "Reload" di Web tab

## Troubleshooting:
- Cek error logs di Web tab
- Pastikan semua path sudah benar
- Cek permissions file/folder