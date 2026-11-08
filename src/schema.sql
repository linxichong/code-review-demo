CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    reference TEXT NOT NULL UNIQUE,
    customer_email TEXT NOT NULL
);
