-- name: create-db-schema#

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32),
    phone_number VARCHAR(32) NOT NULL,
    is_verified BOOLEAN
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    status VARCHAR(32),
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    "count" INTEGER DEFAULT 1,
    order_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (id)
);


-- name: populate#

INSERT INTO customers (first_name, last_name, phone_number, is_verified)
SELECT 'First Name', 'Last Name', '+1 234 567 88 99', true
FROM generate_series(1, 100) AS gs;

INSERT INTO orders (status, customer_id)
SELECT 'status', floor(random() * 100 + 1)::int
FROM generate_series(1, 100000) AS gs;

INSERT INTO order_items (name, price, "count", order_id)
SELECT 'name', floor(random() * 10000 + 1)::int, floor(random() * 10)::int, floor(random() * 1000 + 1)::int
FROM generate_series(1, 100000) as gs;


-- name: drop-db-schema#

DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
