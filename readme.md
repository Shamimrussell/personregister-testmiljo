# Personregister i testmiljön

Ett enkelt system för att hantera testdata på ett GDPR-kompatibelt sätt.

## Funktioner

- Skapa och initiera databas med testanvändare
- Visa alla användare
- Rensa all testdata (GDPR åtgärd 1)
- Anonymisera användardata (GDPR åtgärd 2)

## Installation och körning

### Förutsättningar
- Docker och Docker Compose
- Python 3.9+

##VAD VI TESTAR FÖR GDPR-COMPLIANCE:

init_database() - Säkerställer att vi börjar med en ren, strukturerad databas
populate_fake_users() - Testdata genereras på ett kontrollerat sätt
clear_test_data() - GDPR "Right to erasure" - användare kan radera sin data
anonymize_data() - GDPR "Right to be forgotten" - data anonymiseras snarare än raderas


### Kör med Docker

1. Klona repot:
```bash
git clone <your-repo-url>
cd personregister-testmiljo
