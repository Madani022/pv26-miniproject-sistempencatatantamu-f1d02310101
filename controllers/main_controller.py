from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from views.form_dialog import FormDialog

class MainController:
    def __init__(self, view, db):
        self.view = view
        self.db = db
        
        # Hubungkan signal (tombol diklik) ke slot (fungsi)
        self.view.btn_tambah.clicked.connect(self.add_data)
        self.view.btn_edit.clicked.connect(self.edit_data)
        self.view.btn_hapus.clicked.connect(self.delete_data)
        
        self.load_table_data()

    def load_table_data(self):
        self.view.table.setRowCount(0)
        records = self.db.get_all_data()
        for row_idx, row_data in enumerate(records):
            self.view.table.insertRow(row_idx)
            for col_idx, data in enumerate(row_data):
                self.view.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def add_data(self):
        dialog = FormDialog(self.view, "Tambah Data Tamu")
        if dialog.exec():
            new_data = dialog.get_data()
            self.db.insert_data(new_data)
            self.load_table_data()

    def edit_data(self):
        selected_row = self.view.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.view, "Peringatan", "Pilih data yang ingin diedit terlebih dahulu!")
            return

        # Ambil ID dan data dari baris yang dipilih
        id_tamu = int(self.view.table.item(selected_row, 0).text())
        current_data = (
            self.view.table.item(selected_row, 1).text(),
            self.view.table.item(selected_row, 2).text(),
            self.view.table.item(selected_row, 3).text(),
            self.view.table.item(selected_row, 4).text(),
            self.view.table.item(selected_row, 5).text(),
        )

        dialog = FormDialog(self.view, "Edit Data Tamu")
        dialog.set_data(current_data) # Isi form dengan data lama
        
        if dialog.exec():
            updated_data = dialog.get_data()
            self.db.update_data(id_tamu, updated_data)
            self.load_table_data()

    def delete_data(self):
        selected_row = self.view.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.view, "Peringatan", "Pilih data yang ingin dihapus terlebih dahulu!")
            return

        # Syarat wajib: Dialog Konfirmasi (QMessageBox)
        reply = QMessageBox.question(self.view, "Konfirmasi Hapus", 
                                     "Apakah Anda yakin ingin menghapus data tamu ini?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            id_tamu = int(self.view.table.item(selected_row, 0).text())
            self.db.delete_data(id_tamu)
            self.load_table_data()