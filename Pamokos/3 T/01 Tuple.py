# Isivaizduokime, kad turime duomenų grupę,
# kurią norime saugoti kaip vieną kintamąjį.
# Tai gali būti bet koks dalykas
# Pvz.:
    # Žmogus - vardas, pavardė, amžius, ūgis, svoris
    # Automobilis - markė, modelis, variklio tūris, kuro tipas, kaina
    # Mokykla - pavadinimas, adresas, mokytojų skaičius, mokinių skaičius
    # ir t.t.

# Aišku, kad šiuos duomenis galime saugoti atskiruose kintamuosiuose,
# bet tai bus nepatogu, nes turėsime daug kintamųjų.

# Vienas iš būdų, kaip galime saugoti šiuos duomenis, tai naudojant Masyvus.
# Bet masyvai turi vieną trūkumą - mes galime pamiršti,
# koks elementas ką reiškia, nes masyvai yra numeruojami.

name = "Jonas"
surname = "Jonaitis"
age = 30
height = 1.80
weight = 80

human_arr = [name, surname, age, height, weight]
print(human_arr)

# Kitas programuotojas arba mes patys, po kiek laiko, galime pamiršti,
# kas yra human[0], human[1], human[2] ir t.t.
# Ir skaitydami kodą, turėsime atsiminti, kas yra kas.

# Kitas būdas, kaip galime saugoti duomenis, tai naudojant Tuple.
# Tuple yra nekintamas sąrašas, kuris saugo duomenis pagal jų tvarką.
# Tuple yra naudojamas, kai norime saugoti duomenis, kurie turi savo tvarką.

human_tuple = (name, surname, age, height, weight)
print(human_tuple)

# Tuple yra nekintamas, todėl negalime keisti jo elementų.
# human_tuple.append("test") # AttributeError: 'tuple' object has no attribute 'append'
# human_tuple[0] = "test" # TypeError: 'tuple' object does not support item assignment

# O masivai yra kintami, todėl galime keisti jų elementus.
human_arr[0] = "test"
human_arr.append("test")