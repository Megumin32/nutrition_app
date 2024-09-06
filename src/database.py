import sqlite3

conn = sqlite3.connect('nutrition.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS food (
    id INTEGER PRIMARY KEY,
    name TEXT,
    calories REAL,
    protein REAL,
    fat REAL,
    carbs REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS meal_history (
    id INTEGER PRIMARY KEY,
    date TEXT,
    food_id INTEGER,
    quantity REAL,
    FOREIGN KEY (food_id) REFERENCES food (id)
)
''')

conn.commit()
conn.close()
