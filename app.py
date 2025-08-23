from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Model User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default='user')  # admin atau user
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Model Anggota
class Anggota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.Text)
    telepon = db.Column(db.String(20))
    email = db.Column(db.String(120))
    tanggal_bergabung = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='aktif')  # aktif, nonaktif
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('anggotas', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login berhasil!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username atau password salah!', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        nama_lengkap = request.form['nama_lengkap']
        
        if User.query.filter_by(username=username).first():
            flash('Username sudah digunakan!', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email sudah digunakan!', 'error')
            return render_template('register.html')
        
        user = User(username=username, email=email, nama_lengkap=nama_lengkap)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registrasi berhasil! Silakan login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        total_users = User.query.count()
        total_anggota = Anggota.query.count()
        anggota_aktif = Anggota.query.filter_by(status='aktif').count()
    else:
        total_users = User.query.count()
        total_anggota = Anggota.query.filter_by(user_id=current_user.id).count()
        anggota_aktif = Anggota.query.filter_by(user_id=current_user.id, status='aktif').count()
    
    return render_template('dashboard.html', 
                         total_users=total_users, 
                         total_anggota=total_anggota, 
                         anggota_aktif=anggota_aktif)

@app.route('/anggota')
@login_required
def anggota_list():
    if current_user.role == 'admin':
        anggota_list = Anggota.query.all()
    else:
        anggota_list = Anggota.query.filter_by(user_id=current_user.id).all()
    
    return render_template('anggota_list.html', anggota_list=anggota_list)

@app.route('/anggota/add', methods=['GET', 'POST'])
@login_required
def add_anggota():
    if request.method == 'POST':
        nama = request.form['nama']
        alamat = request.form['alamat']
        telepon = request.form['telepon']
        email = request.form['email']
        
        anggota = Anggota(
            user_id=current_user.id,
            nama=nama,
            alamat=alamat,
            telepon=telepon,
            email=email
        )
        
        db.session.add(anggota)
        db.session.commit()
        
        flash('Anggota berhasil ditambahkan!', 'success')
        return redirect(url_for('anggota_list'))
    
    return render_template('add_anggota.html')

@app.route('/anggota/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_anggota(id):
    anggota = Anggota.query.get_or_404(id)
    
    # Cek apakah user memiliki akses ke anggota ini
    if current_user.role != 'admin' and anggota.user_id != current_user.id:
        flash('Anda tidak memiliki akses ke data ini!', 'error')
        return redirect(url_for('anggota_list'))
    
    if request.method == 'POST':
        anggota.nama = request.form['nama']
        anggota.alamat = request.form['alamat']
        anggota.telepon = request.form['telepon']
        anggota.email = request.form['email']
        anggota.status = request.form['status']
        
        db.session.commit()
        flash('Data anggota berhasil diperbarui!', 'success')
        return redirect(url_for('anggota_list'))
    
    return render_template('edit_anggota.html', anggota=anggota)

@app.route('/anggota/delete/<int:id>')
@login_required
def delete_anggota(id):
    anggota = Anggota.query.get_or_404(id)
    
    # Cek apakah user memiliki akses ke anggota ini
    if current_user.role != 'admin' and anggota.user_id != current_user.id:
        flash('Anda tidak memiliki akses ke data ini!', 'error')
        return redirect(url_for('anggota_list'))
    
    db.session.delete(anggota)
    db.session.commit()
    flash('Anggota berhasil dihapus!', 'success')
    return redirect(url_for('anggota_list'))

@app.route('/users')
@login_required
def users_list():
    if current_user.role != 'admin':
        flash('Anda tidak memiliki akses ke halaman ini!', 'error')
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    return render_template('users_list.html', users=users)

@app.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    if current_user.role != 'admin':
        flash('Anda tidak memiliki akses ke halaman ini!', 'error')
        return redirect(url_for('dashboard'))
    
    user = User.query.get_or_404(id)
    
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.nama_lengkap = request.form['nama_lengkap']
        user.role = request.form['role']
        
        db.session.commit()
        flash('Data user berhasil diperbarui!', 'success')
        return redirect(url_for('users_list'))
    
    return render_template('edit_user.html', user=user)

@app.route('/users/delete/<int:id>')
@login_required
def delete_user(id):
    if current_user.role != 'admin':
        flash('Anda tidak memiliki akses ke halaman ini!', 'error')
        return redirect(url_for('dashboard'))
    
    user = User.query.get_or_404(id)
    
    if user.id == current_user.id:
        flash('Anda tidak dapat menghapus akun sendiri!', 'error')
        return redirect(url_for('users_list'))
    
    db.session.delete(user)
    db.session.commit()
    flash('User berhasil dihapus!', 'success')
    return redirect(url_for('users_list'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Buat admin default jika belum ada
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@example.com',
                nama_lengkap='Administrator',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Admin default dibuat: username=admin, password=admin123")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
