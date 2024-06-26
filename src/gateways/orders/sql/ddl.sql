-- name: create-db-schema#

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32),
    phone_number VARCHAR(32) NOT NULL,
    is_verified BOOLEAN
);

CREATE TABLE "order" (
    id SERIAL PRIMARY KEY,
    status VARCHAR(32),
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer (id)
);

CREATE TABLE order_item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    "count" INTEGER DEFAULT 1,
    order_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES "order" (id)
);


-- name: drop-db-schema#

DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS order_item CASCADE;
DROP TABLE IF EXISTS "order" CASCADE;
