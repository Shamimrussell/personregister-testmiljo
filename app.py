import sqlite3
import os
from faker import Faker

#Skapar en instans av Faker för att generera testdata
fake = Faker('sv_SE')

DB_PATH = os.getenv("DATABASE_PATH", "data/test_users.db") #Databasens sökväg från miljövariabel eller standardvärde

def get_connection():                                       #
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_database(): #initierar databasen och skapar tabellen om den inte finns

    conn = get_connection()
    cursor = conn.cursor()
    
    # Tar bort tabellen om den finns 
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
    
     #Ingen DELETE behövs eftersom tabellen droppades Men vi återställer sekvensen för säkerhets skull
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")

    conn.commit()
    conn.close()

    print("Databas initierad och tabellen skapad.")

def populate_fake_users(amount=100):
    
    # Skapar 'amount' antal faker-användare och lägger in dem i den redan nollställda tabellen.
    # Alla körningar börjar om från en tom tabell (DEL 1 sköter nollställningen).

    conn = get_connection()
    cursor = conn.cursor()

# Genererar och infogar fake-användare
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

def display_users(): # Visar alla användare i databasen
    print("DEBUG: display_users() körs") 
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db') 
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print("\nCurrent users in database:")

    for u in users: #Skriver ut varje användare
        print(f"ID: {u[0]} | Name: {u[1]} | Email: {u[2]} | Address: {u[3]} | Personnummer: {u[4]}")

    conn.close()

#GDPR Action 1: Clear all test data
def clear_test_data(): 
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users')
    conn.commit()
    conn.close()
    print("All test data has been cleared (GDPR compliant)")

#GDPR Action 2: Anonymize user data
def anonymize_data():
    print("DEBUG: anonymize_data() körs") #Bekräftar att funktionen har startat (Bra för att verifiera att funktionen faktiskt anropas)
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')
    print(f"DEBUG: Databassökväg: {db_path}")  
    db_path = os.getenv('DATABASE_PATH', 'data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = "Anonym Användare"')
    conn.commit()
    conn.close()
    print("All user names have been anonymized (GDPR compliant)")

# Huvudprogrammet för att initiera databasen och köra en enkel loop
if __name__ == "__main__":
    init_database()
    try:
        while True:
            pass

    except KeyboardInterrupt:
        print("\nShutting down...")


