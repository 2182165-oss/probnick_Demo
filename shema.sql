-- 1. Таблица пользователей (на основе Users_import.xlsx)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),       -- Фамилия
    first_name VARCHAR(100),      -- Имя
    middle_name VARCHAR(100),     -- Отчество
    login VARCHAR(50) UNIQUE,     -- Логин
    role VARCHAR(50)              -- Роль
);

-- 2. Таблица размеров (на основе Sizes_import.xlsx)
CREATE TABLE IF NOT EXISTS sizes (
    id SERIAL PRIMARY KEY,
    size_value NUMERIC(4,1) UNIQUE -- Размер обуви
);

-- 3. Таблица товаров (на основе Products_import.xlsx)
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    category VARCHAR(100),        -- Категория
    subcategory VARCHAR(100),     -- Подкатегория
    image VARCHAR(255),           -- Изображение
    product_name VARCHAR(255),    -- Наименование товара
    manufacturer VARCHAR(100),    -- Производство
    description TEXT,             -- Описание
    composition TEXT,             -- Состав
    price NUMERIC(10,2)           -- Цена
);

-- 4. Таблица складских остатков (на основе Stock_Items_import.xlsx)
CREATE TABLE IF NOT EXISTS stock_items (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),    -- Наименование товара
    manufacturer VARCHAR(100),    -- Производство
    size NUMERIC(4,1),            -- Размер
    stock_quantity INTEGER        -- Количество доступное для заказа
);

-- 5. Таблица заказов (на основе Orders_import.xlsx)
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    order_number INTEGER,         -- Номер заказа
    order_date DATE,              -- Дата заказа
    customer_name VARCHAR(255),   -- ФИО клиента
    category VARCHAR(100),        -- Категория
    product_name VARCHAR(255),    -- Наименование товара
    manufacturer VARCHAR(100),    -- Производство
    size NUMERIC(4,1),            -- Размер
    quantity INTEGER,             -- Количество
    unit_price NUMERIC(10,2)      -- Цена за единицу
);