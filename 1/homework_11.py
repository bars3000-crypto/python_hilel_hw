import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.executescript("""
CREATE TABLE Owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE Dogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    breed TEXT NOT NULL,
    birth_year INTEGER NOT NULL,
    weight REAL NOT NULL,
    owner_id INTEGER REFERENCES Owners(id)
);

CREATE TABLE Visits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dog_id INTEGER REFERENCES Dogs(id),
    visit_date TEXT NOT NULL,
    reason TEXT NOT NULL,
    price REAL NOT NULL
);

INSERT INTO Owners (name, city, email) VALUES
('Anna Kovalenko', 'Kyiv', 'anna.k@gmail.com'),
('Borys Shevchenko', 'Lviv', 'borys.s@gmail.com'),
('Olena Tkachuk', 'Kyiv', 'olena.t@gmail.com');

INSERT INTO Dogs (name, breed, birth_year, weight, owner_id) VALUES
('Bobik', 'mixed', 2018, 12.4, 1),
('Barsik', 'German Shepherd', 2016, 34.0, 1),
('Max', 'Golden Retriever', 2017, 31.8, 3),
('Sirko', 'mixed', 2015, 18.2, 2);

INSERT INTO Visits (dog_id, visit_date, reason, price) VALUES
(1, '2024-01-15', 'vaccination', 400.0),
(2, '2024-02-10', 'surgery', 3500.0),
(3, '2024-03-05', 'checkup', 300.0),
(2, '2024-04-12', 'dental cleaning', 1200.0),
(4, '2024-05-20', 'injury treatment', 1500.0),
(1, '2024-06-01', 'grooming', 500.0);
""")

print("--- Завдання 1 ---")
cursor.execute("SELECT name, breed, weight FROM Dogs;")
print(cursor.fetchall())

print("\n--- Завдання 2 ---")
cursor.execute("SELECT * FROM Dogs WHERE weight > 25;")
print(cursor.fetchall())

print("\n--- Завдання 3 ---")
cursor.execute("SELECT name, email FROM Owners WHERE city = 'Kyiv';")
print(cursor.fetchall())

print("\n--- Завдання 4 ---")
cursor.execute("SELECT name, birth_year FROM Dogs WHERE breed = 'mixed';")
print(cursor.fetchall())

print("\n--- Завдання 5 ---")
cursor.execute("SELECT reason, visit_date, price FROM Visits ORDER BY price DESC LIMIT 5;")
print(cursor.fetchall())

connection.close()