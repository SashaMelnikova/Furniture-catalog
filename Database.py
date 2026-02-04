import sqlite3

conn = sqlite3.connect("furniture.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS furniture(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               category TEXT,
               price INTEGER,
               material TEXT,
               size TEXT,
               color TEXT,
               available INTEGER CHECK (available IN (0, 1)) DEFAULT 1
               )
""")

catalog = [
    ("Угловой диван", "Диваны", 45000, "Ясень, ткань", "175x100x100", "Тёмно-зелёный", 1),
    ("Кресло", "Диваны", 12000, "Ясень, ткань", "50x50x100", "Чёрный", 1),
    ("Стул", "Стулья", 2000, "Дуб", "45x45x80", "-", 0),
    ("Кровать двуспальная", "Кровати", 50000, "Клён, ткань", "150x200x60", "Белый", 1),
    ("Тахта", "Диваны", 15000, "Ясень, ткань", "130x80x65", "Белый", 0),
    ("Табуретка", "Стулья", 900, "Клён", "50x50x100", "-", 1),
    ("Кровать двуспальная", "Кровати", 55000, "Клён, ткань", "155x190x55", "Бежевый", 1),
    ("Кровать односпальная", "Кровати", 40000, "Металл, ткань", "100x180x55", "Розовый", 1),
    ("Диван", "Диваны", 37000, "Металл, ткань", "160x85x110", "Чёрный", 0),
    ("Офисный стул", "Стулья", 1000, "Металл", "50x50x90", "-", 1)
]

cursor.executemany("INSERT INTO furniture(name, category, price, material, size, color, available) VALUES (?, ?, ?, ?, ?, ?, ?)",
               catalog)

conn.commit()
conn.close()