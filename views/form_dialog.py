from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton

class FormDialog(QDialog):
    def __init__(self, parent=None, title="Tambah Data Tamu"):
        super().__init__(parent)
        self.setWindowTitle(title)
        
        self.layout = QVBoxLayout(self)
        self.form_layout = QFormLayout()
        
        self.input_nama = QLineEdit()
        self.input_instansi = QLineEdit()
        self.input_keperluan = QLineEdit()
        self.input_nohp = QLineEdit()
        self.input_keterangan = QLineEdit()
        
        self.form_layout.addRow("Nama Pemohon:", self.input_nama)
        self.form_layout.addRow("Instansi/Alamat:", self.input_instansi)
        self.form_layout.addRow("Keperluan:", self.input_keperluan)
        self.form_layout.addRow("Nomor HP:", self.input_nohp)
        self.form_layout.addRow("Keterangan:", self.input_keterangan)
        
        self.btn_simpan = QPushButton("Simpan")
        
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.btn_simpan)
        
        self.btn_simpan.clicked.connect(self.accept)

    def get_data(self):
        return (
            self.input_nama.text(),
            self.input_instansi.text(),
            self.input_keperluan.text(),
            self.input_nohp.text(),
            self.input_keterangan.text()
        )

    def set_data(self, data):
        # Fungsi ini dipanggil saat mode Edit
        self.input_nama.setText(data[0])
        self.input_instansi.setText(data[1])
        self.input_keperluan.setText(data[2])
        self.input_nohp.setText(data[3])
        self.input_keterangan.setText(data[4])