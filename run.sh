#!/bin/bash

echo "🚀 Memulai Sistem Manajemen Data..."
echo "=================================="

# Cek apakah virtual environment sudah ada
if [ ! -d "venv" ]; then
    echo "📦 Membuat virtual environment..."
    python -m venv venv
fi

# Install dependencies jika belum
if [ ! -f "venv/lib/python*/site-packages/flask" ]; then
    echo "📥 Installing dependencies..."
    venv/bin/pip install -r requirements.txt
fi

# Jalankan aplikasi
echo "🌐 Menjalankan aplikasi di http://localhost:5000"
echo "🔑 Admin default: username=admin, password=admin123"
echo "⏹️  Tekan Ctrl+C untuk menghentikan"
echo ""

venv/bin/python app.py
