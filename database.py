import psycopg2

# Параметры соединения с БД
CONN_PARAMS = {
    "dbname": "demo",
    "user": "postgres",
    "password": "12345678",
    "host": "localhost",
    "port": "5432"
}


def open_connection():
    """Открывает новое соединение с PostgreSQL."""
    return psycopg2.connect(**CONN_PARAMS)


def check_user(login_value):
    """Проверяет наличие пользователя по логину и возвращает его данные."""
    connection = None
    try:
        connection = open_connection()
        cur = connection.cursor()
        sql = """
            SELECT last_name, first_name, middle_name, role
            FROM users
            WHERE login = %s;
        """
        cur.execute(sql, (login_value,))
        result = cur.fetchone()
        cur.close()
        connection.close()

        if result is None:
            return None

        surname, name, patronymic, user_role = result

        # Формируем короткое ФИО: Иванов И.И.
        short_name = surname
        if name:
            short_name += f" {name[0]}."
        if patronymic:
            short_name += f"{patronymic[0]}."

        role_title = user_role if user_role else "Менеджер"

        return {
            "fio": short_name,
            "role_name": role_title,
            "role_id": user_role
        }

    except Exception as err:
        print(f"Ошибка БД (авторизация): {err}")
        if connection:
            connection.close()
        return None


def fetch_products():
    """Возвращает список товаров с остатками (8 полей на строку)."""
    connection = None
    try:
        connection = open_connection()
        cur = connection.cursor()
        sql = """
            SELECT
                p.id,
                p.product_name,
                p.category,
                p.subcategory,
                p.manufacturer,
                p.composition,
                p.price,
                COALESCE((
                    SELECT SUM(s.stock_quantity)
                    FROM stock_items s
                    WHERE s.product_name = p.product_name
                ), 0) AS qty
            FROM products p;
        """
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        connection.close()
        return data

    except Exception as err:
        print(f"Ошибка БД (товары): {err}")
        if connection:
            connection.close()
        return []


def fetch_categories(cursor=None):
    """Возвращает уникальные категории товаров."""
    own_connection = False
    connection = None
    try:
        if cursor is None:
            connection = open_connection()
            cur = connection.cursor()
            own_connection = True
        else:
            cur = cursor

        cur.execute("SELECT DISTINCT category FROM products WHERE category IS NOT NULL;")
        result = [row[0] for row in cur.fetchall()]

        if own_connection:
            cur.close()
            connection.close()

        return result

    except Exception as err:
        print(f"Ошибка БД (категории): {err}")
        if own_connection and connection:
            connection.close()
        return []


def fetch_orders():
    """Возвращает все заказы."""
    connection = None
    try:
        connection = open_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM orders;")
        data = cur.fetchall()
        cur.close()
        connection.close()
        return data

    except Exception as err:
        print(f"Ошибка получения заказов: {err}")
        if connection:
            connection.close()
        return []


def fetch_order_details(order_number):
    """Возвращает детали заказа по его номеру."""
    connection = None
    try:
        connection = open_connection()
        cur = connection.cursor()
        cur.execute("SELECT * FROM orders WHERE order_number = %s;", (order_number,))
        data = cur.fetchall()
        cur.close()
        connection.close()
        return data

    except Exception as err:
        print(f"Ошибка получения деталей заказа: {err}")
        if connection:
            connection.close()
        return []


def remove_order(order_id):
    """Удаляет заказ по его ID."""
    connection = None
    try:
        connection = open_connection()
        cur = connection.cursor()
        cur.execute("DELETE FROM orders WHERE id = %s;", (order_id,))
        connection.commit()
        cur.close()
        connection.close()
        return True

    except Exception as err:
        print(f"Ошибка удаления заказа: {err}")
        if connection:
            connection.close()
        return False


def save_order(user_fio, cart_items, total_price):
    """Создаёт новый заказ (поведение как раньше)."""
    connection = None
    try:
        connection = open_connection()
        cur = connection.cursor()

        for item in cart_items:
            sql = """
                INSERT INTO orders (order_number, order_date, customer_name, product_name, quantity, unit_price)
                VALUES (DEFAULT, CURRENT_DATE, %s, %s, %s, %s);
            """

        connection.commit()
        cur.close()
        connection.close()
        return True

    except Exception as err:
        print(f"Ошибка сохранения заказа: {err}")
        if connection:
            connection.close()
        return False
