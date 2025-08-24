# Sistem Manajemen Data - Website Localhost

Website sistem manajemen data dengan database SQLite untuk mengelola user dan anggota. Website ini berjalan di localhost dengan fitur login, register, dan manajemen data yang lengkap.

## 🚀 Fitur Utama

### 🔐 Sistem Autentikasi
- **Login/Register**: Sistem autentikasi yang aman dengan password hashing
- **Role-based Access**: Admin dan User dengan hak akses berbeda
- **Session Management**: Manajemen sesi yang aman

### 👥 Manajemen User
- **CRUD User**: Create, Read, Update, Delete data user
- **Role Management**: Pengaturan role admin/user
- **User Dashboard**: Dashboard khusus untuk setiap user

### 📋 Manajemen Anggota
- **Data Anggota**: Kelola informasi anggota (nama, alamat, telepon, email)
- **Status Anggota**: Status aktif/nonaktif
- **Tanggal Bergabung**: Tracking tanggal bergabung anggota

### 📊 Dashboard & Statistik
- **Overview Data**: Statistik total user dan anggota
- **Quick Actions**: Aksi cepat untuk menambah data
- **Responsive Design**: Tampilan yang responsif di semua device

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python Flask
- **Database**: SQLite dengan SQLAlchemy ORM
- **Frontend**: HTML, CSS, Bootstrap 5
- **Authentication**: Flask-Login
- **Icons**: Font Awesome
- **Tables**: DataTables (pencarian, sorting, pagination)

## 📦 Instalasi

### 1. Clone Repository
```bash
git clone <repository-url>
cd webardx1DBT01
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
python app.py
```

### 4. Akses Website
Buka browser dan kunjungi: `http://localhost:5000`

## 🔑 Akun Default

Saat pertama kali menjalankan aplikasi, akan dibuat akun admin default:

- **Username**: `admin`
- **Password**: `admin123`
- **Role**: Administrator

**⚠️ Penting**: Ganti password admin default setelah login pertama kali!

## 📁 Struktur Proyek

```
websiteardx1tester/
├── app.py                 # File utama aplikasi Flask
├── requirements.txt       # Dependencies Python
├── README.md             # Dokumentasi
├── users.db              # Database SQLite (auto-generated)
├── templates/            # Template HTML
│   ├── base.html         # Template dasar
│   ├── index.html        # Halaman beranda
│   ├── login.html        # Halaman login
│   ├── register.html     # Halaman register
│   ├── dashboard.html    # Dashboard utama
│   ├── anggota_list.html # Daftar anggota
│   ├── add_anggota.html  # Form tambah anggota
│   ├── edit_anggota.html # Form edit anggota
│   ├── users_list.html   # Daftar user (admin)
│   └── edit_user.html    # Form edit user
└── static/               # File statis (CSS, JS, images)
    ├── css/
    └── js/
```

## 🎯 Cara Penggunaan

### 1. Login sebagai Admin
1. Buka `http://localhost:5000`
2. Klik "Login"
3. Masukkan username: `admin` dan password: `admin123`
4. Klik "Login"

### 2. Manajemen User (Admin)
- **Lihat Semua User**: Menu "Manajemen User"
- **Tambah User**: Klik "Tambah User" atau akses `/register`
- **Edit User**: Klik icon edit pada tabel user
- **Hapus User**: Klik icon hapus (tidak bisa hapus diri sendiri)

### 3. Manajemen Anggota
- **Lihat Anggota**: Menu "Data Anggota"
- **Tambah Anggota**: Klik "Tambah Anggota"
- **Edit Anggota**: Klik icon edit pada tabel anggota
- **Hapus Anggota**: Klik icon hapus dengan konfirmasi

### 4. Dashboard
- **Statistik**: Lihat total user, anggota, dan anggota aktif
- **Quick Actions**: Aksi cepat untuk menambah data
- **Informasi User**: Detail user yang sedang login

## 🔒 Keamanan

- **Password Hashing**: Password di-hash menggunakan Werkzeug
- **Session Management**: Flask-Login untuk manajemen sesi
- **Role-based Access**: Pembatasan akses berdasarkan role
- **CSRF Protection**: Proteksi terhadap Cross-Site Request Forgery
- **Input Validation**: Validasi input form

## 🎨 Fitur UI/UX

- **Responsive Design**: Tampilan yang responsif di mobile dan desktop
- **Modern UI**: Menggunakan Bootstrap 5 dengan gradient design
- **Interactive Tables**: DataTables dengan pencarian dan sorting
- **Flash Messages**: Notifikasi untuk feedback user
- **Icon Integration**: Font Awesome icons untuk UI yang menarik
- **Sidebar Navigation**: Navigasi yang mudah dan intuitif

## 🐛 Troubleshooting

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Port 5000 already in use"
```bash
# Cari dan matikan proses yang menggunakan port 5000
lsof -ti:5000 | xargs kill -9
```

### Database tidak ter-update
```bash
# Hapus file database dan restart aplikasi
rm users.db
python app.py
```
## Pastikan nih 100%
```bash
chmod +x run.sh
./run.sh
```

## virtual eror gunakan ini
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## 📝 Catatan Penting

1. **Backup Database**: Backup file `users.db` secara berkala
2. **Environment**: Pastikan menggunakan Python 3.7+
3. **Dependencies**: Install semua dependencies di `requirements.txt`
4. **Security**: Ganti SECRET_KEY di `app.py` untuk production
5. **Localhost Only**: Website ini dirancang untuk localhost

## 🤝 Kontribusi

Untuk berkontribusi pada proyek ini:

1. Fork repository
2. Buat branch fitur baru
3. Commit perubahan
4. Push ke branch
5. Buat Pull Request

## 📄 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan penggunaan lokal.

---

**Dibuat dengan ❤️ menggunakan Flask dan Bootstrap**

scyla as dev
archlin as A.I
