#show_users.py
# Script för att visa alla användare i test_users.db

import sqlite3
import os

# Anger sökvägen till databasfil
db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')

if not os.path.exists(db_path):
    print(f"Ingen databas hittades på: {db_path}")
    exit()

# Ansluter till databasen
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Hämtar alla användare
cursor.execute("SELECT id, name, email, address, personnummer FROM users ORDER BY id")
users = cursor.fetchall()

if not users:
    print("Inga användare hittades i databasen.")
else:
    print(f"Totalt {len(users)} användare i databasen:\n")
    for u in users:
        print(f"ID: {u[0]} | Name: {u[1]} | Email: {u[2]} | Address: {u[3]} | Personnummer: {u[4]}")

# Stänger anslutningen
conn.close()
