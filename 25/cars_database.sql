CREATE DATABASE IF NOT EXISTS car_market
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE car_market;

CREATE TABLE IF NOT EXISTS cars (
  car_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  brand VARCHAR(50) NOT NULL,
  model VARCHAR(80) NOT NULL,
  release_year YEAR NOT NULL,
  vin_code VARCHAR(17) NOT NULL,
  added_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  engine_volume DECIMAL(3,1) NOT NULL,
  mileage_km INT UNSIGNED,
  is_customs_cleared BOOLEAN NOT NULL DEFAULT FALSE,
  price DECIMAL(10,2) NOT NULL,
  description TEXT,
  is_sold BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (car_id),
  UNIQUE KEY uq_cars_vin_code (vin_code),
  CONSTRAINT chk_cars_vin_length CHECK (CHAR_LENGTH(vin_code) = 17),
  CONSTRAINT chk_cars_engine_volume CHECK (engine_volume > 0.5),
  CONSTRAINT chk_cars_price CHECK (price >= 0)
);

INSERT INTO cars (
  brand,
  model,
  release_year,
  vin_code,
  engine_volume,
  mileage_km,
  is_customs_cleared,
  price,
  description,
  is_sold
) VALUES
('Toyota', 'Camry', 2018, '4T1B11HK5JU123456', 2.5, 82000, TRUE, 18500.00, 'Comfortable sedan with automatic transmission.', FALSE),
('BMW', '330i', 2020, 'WBA5R1C04LFH12345', 2.0, 46000, TRUE, 32900.00, 'Sport package, leather interior, excellent condition.', FALSE),
('Mercedes-Benz', 'C 300', 2019, '55SWF8DB9KU123456', 2.0, 54000, TRUE, 31000.00, 'Premium sedan with navigation and panoramic roof.', FALSE),
('Honda', 'Civic', 2017, '2HGFC2F59HH123456', 1.5, 97000, FALSE, 13900.00, 'Economical daily car, turbo engine.', FALSE),
('Ford', 'Mustang', 2021, '1FA6P8THXM5123456', 2.3, 23000, TRUE, 36500.00, 'Coupe with EcoBoost engine and sport seats.', FALSE),
('Hyundai', 'Tucson', 2016, 'KM8J33A47GU123456', 2.0, 118000, TRUE, 14500.00, 'Crossover, clean interior, serviced recently.', TRUE),
('Kia', 'Sportage', 2022, 'KNDPM3AC5N7123456', 2.4, 19000, FALSE, 27800.00, 'Low mileage SUV with modern safety features.', FALSE),
('Nissan', 'Leaf', 2018, '1N4AZ1CP6JC123456', 0.7, 61000, TRUE, 11200.00, 'Electric hatchback, battery in good condition.', FALSE),
('Lexus', 'RX 350', 2015, '2T2BK1BA5FC123456', 3.5, 132000, TRUE, 22500.00, 'Luxury SUV, all-wheel drive, well maintained.', TRUE),
('Volkswagen', 'Golf', 2019, '3VWG57AU7KM123456', 1.4, 73000, FALSE, 15800.00, 'Compact hatchback with automatic gearbox.', FALSE);
