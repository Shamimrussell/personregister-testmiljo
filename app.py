import sqlite3
import os
from faker import Faker

#Skapar en instans av Faker för att generera testdata
fake = Faker('sv_SE')

DB_PATH = os.getenv("DATABASE_PATH", "data/test_users.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_database():
    """Initialize the database and create users table"""

    conn = get_connection()
    cursor = conn.cursor()
    
    # Ta bort tabellen om den finns 
    cursor.execute("DROP TABLE IF EXISTS users")
    
    # Skapa tabellen om den inte finns med alla kolumner
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT,
            personnummer TEXT
        )
    """)
    
     #Ingen DELETE behövs eftersom tabellen droppades
    #Men vi återställer sekvensen för säkerhets skull
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")

    conn.commit()
    conn.close()

    print("Databas initierad och tabellen skapad.")

def populate_fake_users(amount=100):
    """
    Skapar 'amount' antal faker-användare och lägger in dem i den redan nollställda tabellen.
    Alla körningar börjar om från en tom tabell (DEL 1 sköter nollställningen).
    """

    conn = get_connection()
    cursor = conn.cursor()

# Generera och infoga fake-användare
    users = []
    for _ in range(amount):
        users.append((
            fake.name(),    
            fake.email(),
            fake.address().replace("\n", ", "),
            fake.ssn()      # Genererar ett svenskt personnummer
        ))

# Använder executemany för att infoga alla användare på en gång
    cursor.executemany("""
        INSERT INTO users (name, email, address, personnummer)
        VALUES (?, ?, ?, ?)
    """, users)

    conn.commit()
    conn.close()

    print(f"{amount} faker-användare har lagts in i databasen.")

def display_users():

#"""Display all users in the database"""
    print("DEBUG: display_users() körs")
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print("\nCurrent users in database:")

    for u in users:
        print(f"ID: {u[0]} | Name: {u[1]} | Email: {u[2]} | Address: {u[3]} | Personnummer: {u[4]}")

    conn.close()

def clear_test_data():

#GDPR Action 1: Clear all test data
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users')
    conn.commit()
    conn.close()
    print("All test data has been cleared (GDPR compliant)")


def anonymize_data():
#GDPR Action 2: Anonymize user data
    print("DEBUG: anonymize_data() körs")  # Lägg till denna rad
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')
    print(f"DEBUG: Databassökväg: {db_path}")  # Lägg till denna rad
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = "Anonym Användare"')
    conn.commit()
    conn.close()
    print("All user names have been anonymized (GDPR compliant)")


if __name__ == "__main__":
    init_database()
    populate_fake_users()


    # Keep the container running for testing
    print("\nContainer is running. Press Ctrl+C to exit.")
    try:
        while True:
            pass

    except KeyboardInterrupt:
        print("\nShutting down...")


