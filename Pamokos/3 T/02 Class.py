# Nors naudojant Tuple, mes galime saugoti duomenis pagal jų tvarką,
# bet mes vis tiek turime atsiminti, kas yra kas.

# Geriau naudoti klases, kurios leidžia saugoti duomenis pagal jų pavadinimus.
# Klase yra kaip brežinys, pagal kurį galime sukurti objektus.
# Objektas yra klasės tipo kintamasis.

# Klases aprašome naudodami class raktinį žodį.
# Klases pavadinimas rašomas CamelCase stiliaus.
# Klases pavadinimas prasideda didžiąja raide.
# Po klasės pavadinimo turi būti dvitaškis.
class Person:  # Klasės pavadinimas Person
    # __init__ metodas (funkcija) yra privalomas.
    # Šis metodas yra vadinamas konstruktoriumi.
    # Konstruktorius yra metodas, kuris yra iškviečiamas,
    # kai sukuriamas naujas objektas.
    def __init__(self, name, surname, age, height, weight):
        # self yra objekto nuoroda.
        # self yra privalomas kiekvienam metode, kuris priklauso klasės.
        # self leidžia pasiekti objekto kintamuosius ir metodus.
        # self yra pirmas argumentas kiekviename metode.
        # self nėra rezervuotas žodis, galima naudoti bet kokį pavadinimą.
        # Bet geriau naudoti self, kad būtų lengviau suprasti kodą.

        # Kintamieji, kurie yra priskiriami objektui,
        # turi būti aprašyti klasės konstruktoriuje.
        # Čia mes priskiriame reikšmes objekto laukams (kintamiesiems).
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight


# Sukuriamas naujas objektas klases Person.
# Naujas objektas yra kintamasis, kuris saugo duomenis.
# Naujas objektas yra sukurtas pagal klasės šabloną.
# Naujas objektas yra klasės tipo kintamasis.

# Kviečiamas konstruktorius ir perduodami parametrai.
person = Person("Jonas", "Jonaitis", 30, 1.80, 80)

# Objekto kintamieji (laukai) pasiekiami naudojant objekto nuorodą.
# Kintamieji yra pasiekiami naudojant tašką.

# Dabar mes galime lengvai pasiekti objekto duomenis
# ir tikrai žinome, kas yra kas, nes duomenys turi pavadinimus.

# Gauname vardą
print(person.name)  # Jonas

# Gauname pavardę
print(person.surname)  # Jonaitis

# Gauname amžių
print(person.age)  # 30

# Gauname ūgį
print(person.height)  # 1.8

# Gauname svorį
print(person.weight)  # 80

# Objekto kintamieji (laukai) gali būti keičiami.

person.name = "Petras"
person.surname = "Petraitis"
person.age = 40
person.height = 1.70
person.weight = 80

print()
print(person.name)  # Petras
print(person.surname)  # Petraitis
print(person.age)  # 40
print(person.height)  # 1.7
print(person.weight)  # 80
