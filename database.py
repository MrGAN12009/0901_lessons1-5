import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("db.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._init_tables()
    

    def _init_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username VARCHAR(15) UNIQUE,
                                password VARCHAR(15),
                                role VARCHAR(15)
                            )
                            """)
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name VARCHAR(25),
                                price REAL
                                )
                            """)
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                                id INTEGER PRIMARY KEY AUTOINCREMENT
                                user_id INTEGER,
                                product_id INTEGER,
                                FOREIGN KEY(user_id) REFERENCES users(id),
                                FOREIGN KEY(product_id) REFERENCES products(id)
                                )
                            """)
        
        admin = self.cursor.fetchone("SELECT * FROM users WHERE username = ?", ("admin",))
        
        if not admin:
            self.cursor.execute("UNSERT INTO users(username, password, role) VALUES (?, ?, ?)",
                                ("admin", "admin", "admin")
                        )

        print("БД инициализирована!")




    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
    
    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    


    
