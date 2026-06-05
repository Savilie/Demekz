-- ============================================================
-- Демонстрационный экзамен 09.02.07 — Вариант №1
-- Создание базы данных "ЧитайГород" (MySQL)
-- ============================================================

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS chitaigorod;
CREATE DATABASE chitaigorod
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE chitaigorod;

-- -------------------------------------------------------
-- 1. Пользователи
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    id          INT          AUTO_INCREMENT PRIMARY KEY,
    role        VARCHAR(50)  NOT NULL COMMENT 'Администратор / Менеджер / Авторизированный клиент',
    full_name   VARCHAR(150) NOT NULL,
    login       VARCHAR(100) NOT NULL UNIQUE,
    password    VARCHAR(50)  NOT NULL,
    INDEX idx_users_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -------------------------------------------------------
-- 2. Производители (издательства)
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS manufacturers (
    id   INT          AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -------------------------------------------------------
-- 3. Поставщики (авторы / поставщики книг)
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS suppliers (
    id   INT          AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -------------------------------------------------------
-- 4. Категории товаров
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS categories (
    id   INT          AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -------------------------------------------------------
-- 5. Товары
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS products (
    article         VARCHAR(20)  NOT NULL PRIMARY KEY COMMENT 'Артикул товара',
    name            VARCHAR(500) NOT NULL,
    unit            VARCHAR(20)  NOT NULL DEFAULT 'шт.',
    price           DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    supplier_id     INT          NOT NULL,
    manufacturer_id INT          NOT NULL,
    category_id     INT          NOT NULL,
    discount        DECIMAL(5,1) NOT NULL DEFAULT 0 CHECK (discount >= 0 AND discount <= 100),
    quantity        INT          NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    description     TEXT         NULL,
    photo           VARCHAR(255) NULL COMMENT 'Имя файла изображения',

    FOREIGN KEY (supplier_id)     REFERENCES suppliers(id)     ON DELETE RESTRICT,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE RESTRICT,
    FOREIGN KEY (category_id)     REFERENCES categories(id)    ON DELETE RESTRICT,

    INDEX idx_products_category (category_id),
    INDEX idx_products_price (price),
    INDEX idx_products_discount (discount)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -------------------------------------------------------
-- 6. Пункты выдачи
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS pickup_points (
    id      INT          AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(300) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -------------------------------------------------------
-- 7. Заказы
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS orders (
    id              INT          AUTO_INCREMENT PRIMARY KEY COMMENT 'Номер заказа',
    order_date      DATE         NOT NULL,
    delivery_date   DATE         NULL,
    pickup_point_id INT          NOT NULL,
    user_id         INT          NOT NULL COMMENT 'Авторизированный клиент',
    pickup_code     INT          NOT NULL COMMENT 'Код для получения',
    status          VARCHAR(30)  NOT NULL DEFAULT 'Новый',

    FOREIGN KEY (pickup_point_id) REFERENCES pickup_points(id) ON DELETE RESTRICT,
    FOREIGN KEY (user_id)         REFERENCES users(id)         ON DELETE RESTRICT,

    INDEX idx_orders_status (status),
    INDEX idx_orders_date (order_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -------------------------------------------------------
-- 8. Состав заказа (для связи M:N)
-- -------------------------------------------------------
CREATE TABLE IF NOT EXISTS order_items (
    id              INT         AUTO_INCREMENT PRIMARY KEY,
    order_id        INT         NOT NULL,
    product_article VARCHAR(20) NOT NULL,
    quantity        INT         NOT NULL CHECK (quantity > 0),

    FOREIGN KEY (order_id)        REFERENCES orders(id)    ON DELETE CASCADE,
    FOREIGN KEY (product_article) REFERENCES products(article) ON DELETE RESTRICT,

    UNIQUE KEY uk_order_product (order_id, product_article),
    INDEX idx_order_items_order (order_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
