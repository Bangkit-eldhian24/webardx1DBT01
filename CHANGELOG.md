# Changelog

Semua perubahan penting untuk proyek ini akan didokumentasikan dalam file ini.

Format berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
dan proyek ini mengikuti [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Fitur baru yang akan datang

### Changed
- Perubahan pada fitur yang ada

### Deprecated
- Fitur yang akan dihapus

### Removed
- Fitur yang dihapus

### Fixed
- Bug fixes

### Security
- Perbaikan keamanan

## [1.0.0] - 2024-08-23

### Added
- Sistem autentikasi dengan login/register
- Manajemen user dengan role admin/user
- Manajemen anggota dengan CRUD lengkap
- Dashboard dengan statistik
- Database SQLite dengan SQLAlchemy ORM
- Interface responsive dengan Bootstrap 5
- DataTables untuk tabel interaktif
- Flash messages untuk feedback user
- Sidebar navigation yang intuitif
- Form validation dan error handling
- Password hashing dengan Werkzeug
- Session management dengan Flask-Login

### Security
- Password hashing untuk keamanan
- Role-based access control
- Input validation untuk mencegah injection
- CSRF protection
- Secure session management

### Technical
- Flask 2.3.3 sebagai web framework
- SQLAlchemy 3.0.5 untuk ORM
- Flask-Login 0.6.3 untuk autentikasi
- Bootstrap 5 untuk UI framework
- Font Awesome untuk icons
- DataTables untuk tabel interaktif

## [0.1.0] - 2024-08-23

### Added
- Initial project setup
- Basic Flask application structure
- Database models (User, Anggota)
- Basic templates and routing
- Development environment setup

---

## Cara Menambahkan Entri Changelog

### Untuk Fitur Baru
```markdown
### Added
- Deskripsi fitur baru
```

### Untuk Perubahan
```markdown
### Changed
- Deskripsi perubahan
```

### Untuk Bug Fix
```markdown
### Fixed
- Deskripsi bug yang diperbaiki
```

### Untuk Keamanan
```markdown
### Security
- Deskripsi perbaikan keamanan
```

## Versi

- **MAJOR**: Perubahan yang tidak kompatibel dengan versi sebelumnya
- **MINOR**: Fitur baru yang kompatibel dengan versi sebelumnya
- **PATCH**: Bug fixes yang kompatibel dengan versi sebelumnya
