from database import Database


class User:
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

    @staticmethod
    def login(username, password):
        db = Database()
        user = db.fetchone(f"SELECT * FROM users WHERE username = ? and password = ?",
                          (username, password))
        
        if user:
            return User(user["id"], user["username"], user["role"])
        
        return None
        
        
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    @staticmethod
    def get_all():
        db = Database()
        rows = db.fetchall("SELECT * FROM products;")
        ret = []
        for r in rows:
            ret.append(Product(r["id"], r["name"], r["price"]))

        return ret

    @staticmethod
    def create(name, price):
        db = Database()
        db.execute("INSERT INTO products (name, price) VALUES (?, ?)",
        (name, price))


class Order:
    def __init__(self, id, user_id, product_id):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id


    @staticmethod
    def get_all():
        db = Database()
        rows = db.fetchall("SELECT * FROM orders;")
        ret = []
        for r in rows:
            ret.append(Order(r["id"], r["user_id"], r["product_id"]))

        return ret




    @staticmethod
    def create(user_id, product_id):
        db = Database()
        db.execute("INSERT INTO orders (user_id, product_id) VALUES (?, ?)",
                   (user_id, product_id))
