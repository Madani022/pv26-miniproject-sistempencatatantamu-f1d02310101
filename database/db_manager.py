import sqlite3

class DBManager:
    def __init__(self, db_name="data_tamu.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS buku_tamu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            instansi TEXT,
            keperluan TEXT,
            no_hp TEXT,
            keterangan TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_data(self, data):
        query = "INSERT INTO buku_tamu (nama, instansi, keperluan, no_hp, keterangan) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, data)
        self.conn.commit()
        
    def get_all_data(self):
        cursor = self.conn.execute("SELECT * FROM buku_tamu")
        return cursor.fetchall()

    def update_data(self, id_tamu, data):
        # data berisi tuple: (nama, instansi, keperluan, no_hp, keterangan)
        query = "UPDATE buku_tamu SET nama=?, instansi=?, keperluan=?, no_hp=?, keterangan=? WHERE id=?"
        self.conn.execute(query, (*data, id_tamu))
        self.conn.commit()

    def delete_data(self, id_tamu):
        query = "DELETE FROM buku_tamu WHERE id=?"
        self.conn.execute(query, (id_tamu,))
        self.conn.commit()