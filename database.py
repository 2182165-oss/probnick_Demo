import psycopg2

DB_CONFIG = {
    "dbname": "demo",
    "user": "postgres",
    "password": "12345678",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def authenticate_user(login):
    """Авторизация пользователя по логину"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT last_name, first_name, middle_name, role
            FROM users
            WHERE login = %s;
        """
        cursor.execute(query, (login,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data:
            last_name, first_name, middle_name, role = user_data
            fio = f"{last_name} {first_name[0]}." if first_name else last_name
            if middle_name:
                fio += f"{middle_name[0]}."
           
            role_name = role if role else "Менеджер"
            return {"fio": fio, "role_name": role_name, "role_id": role}
        return None
    except Exception as e:
        print(f"Ошибка БД (авторизация): {e}")
        return None

def get_all_products():
    """Получение всех товаров (ровно 8 элементов под распаковку в main.py)"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Возвращаем ровно 8 полей: id, name, category, subcategory, manufacturer, composition, price, qty
        query = """
            SELECT
                p.id,
                p.product_name,
                p.category,
                p.subcategory,
                p.manufacturer,
                p.composition,
                p.price,
                COALESCE((SELECT SUM(s.stock_quantity) FROM stock_items s WHERE s.product_name = p.product_name), 0) as qty
            FROM products p;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Ошибка БД (товары): {e}")
        return []

def get_all_categories(cur=None):
    """Возвращает список всех уникальных категорий товаров."""
    close_conn = False
    try:
        if cur is None:
            conn = get_connection()
            cursor = conn.cursor()
            close_conn = True
        else:
            cursor = cur
           
        cursor.execute("SELECT DISTINCT category FROM products WHERE category IS NOT NULL;")
        categories = [row[0] for row in cursor.fetchall()]
       
        if close_conn:
            cursor.close()
            conn.close()
        return categories
    except Exception as e:
        print(f"Ошибка БД (категории): {e}")
        return []

def get_all_orders():
    """Получение всех заказов"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM orders;"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Ошибка получения заказов: {e}")
        return []

def get_order_details(order_number):
    """Возвращает детальную информацию по конкретному заказу по его номеру."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM orders WHERE order_number = %s;"
        cursor.execute(query, (order_number,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        print(f"Ошибка получения деталей заказа: {e}")
        return []

def delete_order_by_id(order_id):
    """Удаление заказа по его ID."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM orders WHERE id = %s;"
        cursor.execute(query, (order_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Ошибка удаления заказа: {e}")
        return False

def create_order(user_fio, cart_items, total_price):
    """Создание заказа"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        for item in cart_items:
            query_order = """
                INSERT INTO orders (order_number, order_date, customer_name, product_name, quantity, unit_price)
                VALUES (DEFAULT, CURRENT_DATE, %s, %s, %s, %s);
            """
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Ошибка сохранения заказа: {e}")
        return False