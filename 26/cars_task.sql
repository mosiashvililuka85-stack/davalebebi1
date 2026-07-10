CREATE DATABASE car_market;

USE car_market;

CREATE TABLE cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    release_year YEAR NOT NULL,
    vin_code VARCHAR(17) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    engine_volume DECIMAL(3, 1) CHECK (engine_volume > 0.5),
    mileage_km INT,
    is_customs_cleared BOOLEAN,
    price DECIMAL(10, 2),
    description TEXT,
    is_sold BOOLEAN
);

INSERT INTO cars
    (brand, model, release_year, vin_code, engine_volume, mileage_km, is_customs_cleared, price, description, is_sold)
VALUES
    ('BMW', 'E46', 2004, 'WBABN534X4PJ12345', 2.5, 210000, TRUE, 4500.00, 'Good condition, manual gearbox', FALSE),
    ('Mercedes', 'C200', 2012, 'WDDGF4HB1CR123456', 1.8, 165000, TRUE, 7200.00, 'Clean interior and automatic gearbox', FALSE),
    ('Toyota', 'Prius', 2014, 'JTDKN3DUXE0123456', 1.8, 190000, TRUE, 6800.00, 'Hybrid, low fuel consumption', FALSE),
    ('Honda', 'Fit', 2008, 'JHMGD38408S123456', 1.3, 155000, FALSE, 3900.00, 'Economical city car', TRUE),
    ('Ford', 'Focus', 2011, '1FAHP3FNXBW123456', 2.0, 175000, TRUE, 4300.00, 'Reliable family car', FALSE),
    ('Nissan', 'Leaf', 2015, '1N4AZ0CPXFC123456', 0.6, 98000, TRUE, 5000.00, 'Electric vehicle', TRUE),
    ('Hyundai', 'Elantra', 2017, 'KMHDH4AE5HU123456', 1.6, 120000, TRUE, 8300.00, 'Comfortable sedan', FALSE),
    ('Volkswagen', 'Golf', 2009, 'WVWZZZ1KZ9W123456', 1.6, 230000, FALSE, 3500.00, 'Diesel engine', TRUE),
    ('Audi', 'A4', 2013, 'WAUFFAFL6DN123456', 2.0, 180000, TRUE, 7800.00, 'Quattro, good tires', FALSE),
    ('Kia', 'Sportage', 2016, 'KNDPMCACXG7123456', 2.4, 145000, TRUE, 9900.00, 'SUV, full package', FALSE);

SELECT *
FROM cars;

SELECT brand, model, release_year, price
FROM cars;

SELECT *
FROM cars
WHERE brand = 'BMW';

SELECT *
FROM cars
WHERE price BETWEEN 2000 AND 5000;

SELECT *
FROM cars
WHERE release_year > 2010
  AND is_customs_cleared = TRUE;

SELECT *
FROM cars
WHERE is_sold = FALSE;

SELECT *
FROM cars
WHERE engine_volume > 2.0;

DELETE FROM cars
WHERE car_id IN (1, 2);

DELETE FROM cars
WHERE is_sold = TRUE;

DELETE FROM cars;

TRUNCATE TABLE cars;

DROP TABLE cars;
