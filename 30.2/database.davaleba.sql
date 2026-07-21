DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS customers CASCADE;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    city VARCHAR(60) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    product_name VARCHAR(100) NOT NULL,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0),
    status VARCHAR(30) NOT NULL DEFAULT 'pending',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (full_name, email, city)
VALUES
    ('Nino Beridze', 'nino@example.com', 'Tbilisi'),
    ('Giorgi Maisuradze', 'giorgi@example.com', 'Batumi'),
    ('Mariam Gelashvili', 'mariam@example.com', 'Kutaisi');

INSERT INTO orders (customer_id, product_name, amount, status)
VALUES
    (1, 'Laptop', 2500.00, 'paid'),
    (1, 'Mouse', 55.00, 'pending'),
    (2, 'Keyboard', 180.00, 'paid'),
    (3, 'Monitor', 900.00, 'cancelled');

CREATE VIEW v_all_customers AS
SELECT *
FROM customers;

CREATE VIEW v_paid_orders AS
SELECT *
FROM orders
WHERE status = 'paid';

CREATE VIEW v_customers_orders AS
SELECT
    c.id AS customer_id,
    c.full_name,
    c.email,
    c.city,
    c.updated_at AS customer_updated_at,
    o.id AS order_id,
    o.product_name,
    o.amount,
    o.status,
    o.updated_at AS order_updated_at
FROM customers c
JOIN orders o ON o.customer_id = c.id;

CREATE OR REPLACE VIEW v_paid_orders AS
SELECT *
FROM orders
WHERE status = 'pending';

CREATE OR REPLACE VIEW v_customers_orders AS
SELECT
    c.id AS customer_id,
    c.full_name,
    c.email,
    c.city,
    c.updated_at AS customer_updated_at,
    o.id AS order_id,
    o.product_name,
    o.amount,
    o.status,
    o.updated_at AS order_updated_at,
    (c.full_name || ' - ' || o.product_name) AS customer_order_name
FROM customers c
JOIN orders o ON o.customer_id = c.id;

DROP VIEW IF EXISTS v_customers_orders;
DROP VIEW IF EXISTS v_paid_orders;
DROP VIEW IF EXISTS v_all_customers;

CREATE OR REPLACE PROCEDURE delete_customer_by_id(p_customer_id INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM customers
    WHERE id = p_customer_id;
END;
$$;

CREATE OR REPLACE PROCEDURE update_customer_city(
    p_customer_id INTEGER,
    p_city VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE customers
    SET city = p_city
    WHERE id = p_customer_id;
END;
$$;

CREATE OR REPLACE FUNCTION set_customer_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_set_customer_updated_at
BEFORE UPDATE ON customers
FOR EACH ROW
EXECUTE FUNCTION set_customer_updated_at();
