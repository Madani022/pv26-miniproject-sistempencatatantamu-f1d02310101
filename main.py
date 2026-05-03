import sys
from PySide6.QtWidgets import QApplication
from database.db_manager import DBManager
from views.main_window import MainWindow
from controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)
    
    # Load styling eksternal (Pastikan file styles/style.qss ada)
    try:
        with open("styles/style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: File style.qss tidak ditemukan. Aplikasi tetap berjalan tanpa styling.")
        
    # Inisialisasi komponen (SoC)
    db = DBManager()
    view = MainWindow()
    controller = MainController(view, db) # Controller yang mengatur semuanya
    
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()