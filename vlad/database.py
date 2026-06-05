# database.py — работа с MySQL
import mysql.connector
from config import DB_CONFIG


class Database:
    def __init__(self):
        self.conn = None
        self.connect()

    def connect(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.conn.autocommit = True

    def close(self):
        if self.conn:
            self.conn.close()

    def execute(self, query, params=None):
        cur = self.conn.cursor(dictionary=True)
        cur.execute(query, params or ())
        result = cur.fetchall()
        cur.close()
        return result

    def execute_insert(self, query, params=None):
        cur = self.conn.cursor()
        cur.execute(query, params or ())
        last_id = cur.lastrowid
        cur.close()
        return last_id

    # === Пользователи ===
    def auth_user(self, login, password):
        rows = self.execute(
            "SELECT id, role, full_name FROM users WHERE login = %s AND password = %s",
            (login, password),
        )
        return rows[0] if rows else None

    # === Категории ===
    def get_categories(self):
        return self.execute("SELECT id, name FROM categories ORDER BY name")

    # === Производители ===
    def get_manufacturers(self):
        return self.execute("SELECT id, name FROM manufacturers ORDER BY name")

    # === Поставщики ===
    def get_suppliers(self):
        return self.execute("SELECT id, name FROM suppliers ORDER BY name")

    # === Товары ===
    def get_products(self, search=None, sort_by=None, sort_order="ASC", discount_range=None):
        query = """
            SELECT p.*, c.name AS category_name, m.name AS manufacturer_name,
                   s.name AS supplier_name
            FROM products p
            JOIN categories c ON p.category_id = c.id
            JOIN manufacturers m ON p.manufacturer_id = m.id
            JOIN suppliers s ON p.supplier_id = s.id
            WHERE 1=1
        """
        params = []

        if search:
            query += " AND (p.article LIKE %s OR p.name LIKE %s OR p.description LIKE %s OR c.name LIKE %s OR m.name LIKE %s OR s.name LIKE %s)"
            like = f"%{search}%"
            params.extend([like] * 6)

        if discount_range == "0-12.99":
            query += " AND p.discount BETWEEN 0 AND 12.99"
        elif discount_range == "13-16.99":
            query += " AND p.discount BETWEEN 13 AND 16.99"
        elif discount_range == "17+":
            query += " AND p.discount >= 17"

        if sort_by in ("price", "quantity"):
            query += f" ORDER BY p.{sort_by} {sort_order}"
        else:
            query += " ORDER BY p.name"

        return self.execute(query, tuple(params))

    def get_product(self, article):
        rows = self.execute(
            """SELECT p.*, c.name AS category_name, m.name AS manufacturer_name,
                      s.name AS supplier_name
               FROM products p
               JOIN categories c ON p.category_id = c.id
               JOIN manufacturers m ON p.manufacturer_id = m.id
               JOIN suppliers s ON p.supplier_id = s.id
               WHERE p.article = %s""",
            (article,),
        )
        return rows[0] if rows else None

    def add_product(self, data):
        self.execute_insert(
            """INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id,
               category_id, discount, quantity, description, photo)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                data["article"], data["name"], data["unit"], data["price"],
                data["supplier_id"], data["manufacturer_id"], data["category_id"],
                data["discount"], data["quantity"], data["description"], data["photo"],
            ),
        )

    def update_product(self, article, data):
        self.execute(
            """UPDATE products SET name=%s, unit=%s, price=%s, supplier_id=%s,
               manufacturer_id=%s, category_id=%s, discount=%s, quantity=%s,
               description=%s, photo=%s WHERE article=%s""",
            (
                data["name"], data["unit"], data["price"],
                data["supplier_id"], data["manufacturer_id"], data["category_id"],
                data["discount"], data["quantity"], data["description"], data["photo"],
                article,
            ),
        )

    def delete_product(self, article):
        self.execute("DELETE FROM products WHERE article = %s", (article,))

    def product_in_orders(self, article):
        rows = self.execute(
            "SELECT COUNT(*) AS cnt FROM order_items WHERE product_article = %s",
            (article,),
        )
        return rows[0]["cnt"] > 0

    # === Пункты выдачи ===
    def get_pickup_points(self):
        return self.execute("SELECT id, address FROM pickup_points ORDER BY address")

    # === Заказы ===
    def get_orders(self):
        return self.execute(
            """SELECT o.*, u.full_name AS user_name
               FROM orders o
               JOIN users u ON o.user_id = u.id
               ORDER BY o.id"""
        )

    def get_order_items(self, order_id):
        return self.execute(
            """SELECT oi.*, p.name AS product_name
               FROM order_items oi
               JOIN products p ON oi.product_article = p.article
               WHERE oi.order_id = %s""",
            (order_id,),
        )

    def add_order(self, data):
        return self.execute_insert(
            """INSERT INTO orders (order_date, delivery_date, pickup_point_id, user_id, pickup_code, status)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                data["order_date"], data.get("delivery_date"),
                data["pickup_point_id"], data["user_id"],
                data["pickup_code"], data["status"],
            ),
        )

    def update_order(self, order_id, data):
        self.execute(
            """UPDATE orders SET order_date=%s, delivery_date=%s, pickup_point_id=%s,
               user_id=%s, pickup_code=%s, status=%s WHERE id=%s""",
            (
                data["order_date"], data.get("delivery_date"),
                data["pickup_point_id"], data["user_id"],
                data["pickup_code"], data["status"], order_id,
            ),
        )

    def delete_order(self, order_id):
        self.execute("DELETE FROM orders WHERE id = %s", (order_id,))
