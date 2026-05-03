from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
                               QTableWidget, QPushButton, QLabel, QMessageBox, 
                               QAbstractItemView, QHeaderView)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt # <-- Tambahkan import Qt untuk alignment text

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistem Pencatatan Tamu")
        
        self.resize(850, 600)
        self.setMinimumSize(600, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        
        # --- TAMBAHAN: Judul Aplikasi Utama ---
        self.label_judul = QLabel("SISTEM PENCATATAN TAMU")
        self.label_judul.setObjectName("judul_aplikasi") # ID khusus untuk QSS
        self.label_judul.setAlignment(Qt.AlignCenter) # Bikin posisinya di tengah
        self.layout.addWidget(self.label_judul)
        
        # Identitas Mahasiswa
        self.label_identitas = QLabel("Nama: Ahmad Madani | NIM: F1D02310101")
        self.label_identitas.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_identitas)
        
        # Tabel Data
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Nama Pemohon", "Instansi", "Keperluan", "No HP", "Keterangan"])
        self.table.setColumnHidden(0, True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.layout.addWidget(self.table)
        
        # Layout Tombol Aksi
        self.btn_layout = QHBoxLayout()
        self.btn_tambah = QPushButton("Tambah Tamu")
        self.btn_edit = QPushButton("Edit Terpilih")
        
        self.btn_hapus = QPushButton("Hapus Terpilih")
        self.btn_hapus.setObjectName("btn_hapus") # <-- Tambahkan ini agar tombol hapus bisa berwarna merah di QSS
        
        self.btn_layout.addWidget(self.btn_tambah)
        self.btn_layout.addWidget(self.btn_edit)
        self.btn_layout.addWidget(self.btn_hapus)
        self.layout.addLayout(self.btn_layout)
        
        self.setup_menu()

    def setup_menu(self):
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu("Tentang Aplikasi")
        
        about_action = QAction("Informasi Pembuat", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def show_about(self):
        QMessageBox.information(self, "Tentang Aplikasi", "Sistem Pencatatan Tamu v1.0\nDibuat oleh: Ahmad Madani\nNIM: F1D02310101\n\nUntuk memenuhi Tugas Mini Project Pemrograman Visual.")