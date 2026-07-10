DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS guests;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS hotels;

CREATE TABLE hotels (
    hotel_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    stars INTEGER NOT NULL CHECK (stars BETWEEN 1 AND 5)
);

CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    hotel_id INTEGER NOT NULL,
    room_number VARCHAR(20) NOT NULL,
    floor INTEGER NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL CHECK (price_per_night > 0),
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id) ON DELETE CASCADE
);

CREATE TABLE guests (
    guest_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
);

CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
);

INSERT INTO hotels (name, city, stars) VALUES
('Tbilisi Palace', 'Tbilisi', 5),
('Batumi Sea View', 'Batumi', 4);

INSERT INTO rooms (hotel_id, room_number, floor, price_per_night) VALUES
(1, '101', 1, 180.00),
(1, '102', 1, 200.00),
(1, '201', 2, 260.00),
(2, '301', 3, 150.00),
(2, '302', 3, 170.00),
(2, '401', 4, 220.00),
(2, '402', 4, 240.00);

INSERT INTO guests (room_id, first_name, last_name, phone) VALUES
(1, 'Giorgi', 'Beridze', '+995 555 11 11 11'),
(1, 'Nino', 'Kapanadze', '+995 555 22 22 22'),
(2, 'Luka', 'Maisuradze', '+995 555 33 33 33'),
(2, 'Mariam', 'Lomidze', '+995 555 44 44 44'),
(3, 'Ana', 'Chkheidze', '+995 555 55 55 55'),
(3, 'Davit', 'Gelashvili', '+995 555 66 66 66'),
(4, 'Saba', 'Tskitishvili', '+995 555 77 77 77'),
(4, 'Elene', 'Abashidze', '+995 555 88 88 88'),
(5, 'Irakli', 'Kiknadze', '+995 555 99 99 99'),
(5, 'Tamar', 'Japaridze', '+995 555 10 10 10'),
(6, 'Mate', 'Nadiradze', '+995 555 12 12 12'),
(6, 'Salome', 'Gogoladze', '+995 555 13 13 13'),
(7, 'Beka', 'Dolidze', '+995 555 14 14 14'),
(7, 'Keti', 'Tsintsadze', '+995 555 15 15 15');

INSERT INTO services (room_id, service_name, price) VALUES
(1, 'Breakfast', 35.00),
(1, 'Laundry', 25.00),
(2, 'Spa', 90.00),
(2, 'Room cleaning', 20.00),
(3, 'Airport transfer', 70.00),
(3, 'Dinner', 60.00),
(4, 'Breakfast', 30.00),
(4, 'Parking', 15.00),
(5, 'Mini bar', 45.00),
(5, 'Laundry', 25.00),
(6, 'Spa', 80.00),
(6, 'Dinner', 55.00);

-- ყველა ნომერი შესაბამისი სასტუმროს სახელთან ერთად
SELECT
    r.room_id,
    r.room_number,
    r.floor,
    r.price_per_night,
    h.name AS hotel_name
FROM rooms r
JOIN hotels h ON r.hotel_id = h.hotel_id;

-- ყველა სტუმარი მისი ნომრის ნომრითა და სასტუმროს სახელით
SELECT
    g.guest_id,
    g.first_name,
    g.last_name,
    g.phone,
    r.room_number,
    h.name AS hotel_name
FROM guests g
JOIN rooms r ON g.room_id = r.room_id
JOIN hotels h ON r.hotel_id = h.hotel_id;

-- კონკრეტული სასტუმროს ყველა სტუმარი
SELECT
    g.guest_id,
    g.first_name,
    g.last_name,
    r.room_number,
    h.name AS hotel_name
FROM guests g
JOIN rooms r ON g.room_id = r.room_id
JOIN hotels h ON r.hotel_id = h.hotel_id
WHERE h.name = 'Tbilisi Palace';

-- თითო სასტუმროში არსებული ნომრების რაოდენობა
SELECT
    h.hotel_id,
    h.name AS hotel_name,
    COUNT(r.room_id) AS rooms_count
FROM hotels h
LEFT JOIN rooms r ON h.hotel_id = r.hotel_id
GROUP BY h.hotel_id, h.name;

-- იმ ნომრები, რომელთათვისაც სერვისი ჯერ არ არის შეკვეთილი
SELECT
    r.room_id,
    r.room_number,
    h.name AS hotel_name
FROM rooms r
JOIN hotels h ON r.hotel_id = h.hotel_id
LEFT JOIN services s ON r.room_id = s.room_id
WHERE s.service_id IS NULL;

-- ერთი ნომრის წაშლა: მასთან დაკავშირებული სტუმრები და სერვისები ავტომატურად წაიშლება
DELETE FROM rooms
WHERE room_id = 1;

-- კონკრეტული ნომრის ღირებულების შეცვლა
UPDATE rooms
SET price_per_night = 210.00
WHERE room_id = 2;

-- ერთი სტუმრის სხვა ნომერზე გადაყვანა
UPDATE guests
SET room_id = 3
WHERE guest_id = 3;
