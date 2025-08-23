# Kebijakan Keamanan

## Versi yang Didukung

Gunakan bagian ini untuk memberi tahu orang tentang versi proyek Anda yang saat ini didukung dengan pembaruan keamanan.

| Versi | Didukung          |
| ----- | ----------------- |
| 1.0.x | :white_check_mark: |

## Melaporkan Kerentanan

Kami sangat menghargai upaya komunitas untuk meningkatkan keamanan proyek kami. Jika Anda menemukan kerentanan keamanan, silakan ikuti langkah-langkah berikut:

### 1. Jangan Membuat Issue Publik
**JANGAN** membuat issue publik untuk kerentanan keamanan. Ini dapat mengekspos pengguna lain terhadap risiko.

### 2. Laporkan Secara Privat
Kirim email ke [bangkiteldhianepp@gmail.com] dengan subjek:
```
[SECURITY] Deskripsi singkat kerentanan
```

### 3. Informasi yang Diperlukan
Sertakan informasi berikut dalam laporan Anda:

- **Deskripsi kerentanan**: Penjelasan detail tentang kerentanan
- **Langkah reproduksi**: Langkah-langkah untuk mereproduksi masalah
- **Dampak potensial**: Bagaimana kerentanan dapat dieksploitasi
- **Saran perbaikan**: Jika Anda memiliki saran untuk memperbaiki
- **Environment**: OS, versi Python, versi aplikasi

### 4. Timeline Response
- **24 jam**: Konfirmasi penerimaan laporan
- **72 jam**: Update status investigasi
- **7 hari**: Rilis patch keamanan (jika diperlukan)

## Praktik Keamanan yang Dianjurkan

### Untuk Pengguna
1. **Update Regular**: Selalu gunakan versi terbaru
2. **Environment Variables**: Jangan hardcode credentials
3. **HTTPS**: Gunakan HTTPS di production
4. **Backup**: Backup database secara regular
5. **Access Control**: Batasi akses ke sistem

### Untuk Developer
1. **Input Validation**: Validasi semua input user
2. **SQL Injection**: Gunakan parameterized queries
3. **XSS Protection**: Escape output HTML
4. **CSRF Protection**: Implementasi CSRF tokens
5. **Password Security**: Hash password dengan bcrypt/werkzeug

## Disclosure Policy

Kami mengikuti kebijakan disclosure yang bertanggung jawab:

1. **Private Disclosure**: Kerentanan dilaporkan secara private
2. **Investigation**: Tim keamanan menyelidiki laporan
3. **Fix Development**: Patch dikembangkan jika diperlukan
4. **Testing**: Patch ditest secara menyeluruh
5. **Release**: Patch dirilis dengan update keamanan
6. **Public Disclosure**: Kerentanan diumumkan setelah patch tersedia

## Credits

Kami akan memberikan credit kepada reporter keamanan di:
- Release notes
- Security advisory
- Hall of fame (jika diinginkan)

## Contact

Untuk pertanyaan keamanan:
- Email: [bangkiteldhianpp@gmail.com]
- PGP Key: [LINK_KE_PGP_KEY_ANDA]

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Security Documentation](https://flask-security.readthedocs.io/)
- [Python Security Best Practices](https://python-security.readthedocs.io/)

---

**Terima kasih atas kontribusi Anda untuk keamanan proyek ini!** 🛡️
