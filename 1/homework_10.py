import sqlite3

connection = sqlite3.connect("books_db.sqlite")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    price REAL
);
""")

books_data = [
    ("Кобзар", "Тарас Шевченко", 1840, 350.00),
    ("1984", "Джордж Орвелл", 1949, 280.50),
    ("Відьмак", "Анджей Сапковський", 1993, 420.00),
    ("Володар перснів", "Дж. Р. Р. Толкін", 1954, 450.00),
    ("Гаррі Поттер", "Дж. К. Роулінг", 1997, 390.00)
]

cursor.executemany("""
INSERT INTO books (title, author, year, price)
VALUES (?, ?, ?, ?);
""", books_data)
connection.commit()

cursor.execute("""
UPDATE books
SET price = 310.00
WHERE id = 2;
""")
connection.commit()

cursor.execute("""
DELETE FROM books
WHERE id = 3;
""")
connection.commit()

cursor.execute("SELECT * FROM books;")
for book in cursor.fetchall():
    print(book)

connection.close()