# Personregister i testmiljön

Ett enkelt system för att hantera testdata på ett GDPR-kompatibelt sätt. Systemet använder en SQLite-databas för att lagra testanvändare med svenska personuppgifter.

## Funktioner

- Skapa och initiera databas med testanvändare
- Visa alla användare
- Rensa all testdata (GDPR åtgärd 1)
- Anonymisera användardata (GDPR åtgärd 2)

## VAD VI TESTAR FÖR GDPR-COMPLIANCE:

### 1. `init_database()`
**Vad det gör:** Skapar en ny, ren databastabell från början varje gång.
**GDPR-anledning:** Säkerställer att vi alltid börjar med en strukturerad och tom databas när vi testar.

### 2. `populate_fake_users()`
**Vad det gör:** Genererar 100 testanvändare med svenska namn, adresser och personnummer.
**GDPR-anledning:** Använder Faker-biblioteket för att skapa realistisk testdata **utan att använda riktiga personuppgifter**.

### 3. `clear_test_data()`
**Vad det gör:** Tar bort ALL data från databasen.
**GDPR-anledning:** Möjliggör "Rätten att bli raderad" (Right to erasure) - användare kan begära att deras data tas bort helt.

### 4. `anonymize_data()`
**Vad det gör:** Ändrar alla namn i databasen till "Anonym Användare".
**GDPR-anledning:** Möjliggör "Rätten att bli bortglömd" (Right to be forgotten) - data anonymiseras istället för att raderas, vilket ibland behövs för statistik eller historiska data.

## Installation och körning

### Förutsättningar
- Docker och Docker Compose
- Python 3.9+
- Git (för att klona repot)

### Kör med Docker (enklaste sättet)

1. Klona repot och navigera till mappen:
```bash
git clone <your-repo-url>
cd personregister-testmiljo