# Jei mes norime atlikti tam tikrą veiksmą tam tikrą kartų, galime naudoti for ciklą.

# Galime tiesiog kartoti kodą kiek reikia
print("Durnas variantas:")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print()

# Bet paprasčiau ir greičiau yra naudoti for ciklą
# For ciklas leidžia mums kartoti kodą tam tikrą kartų
print("Geresnis variantas:")
for _ in range(5):  # For ciklas kartos kodą 5 kartus
    print("Hello World")
print()

# For ciklas turi tris dalis:
# 1. Kintamasis, kuris bus naudojamas kaip skaitiklis (šiuo atveju i)
# 2. Skaitiklio ribos (šiuo atveju range(5). Skaitiklis bus nuo 0 iki 5 (neįskaitant 5))
# 3. Kodas, kuris bus kartojamas (šiuo atveju print(i)). Šis kodas turi būti atskirtas tabuliacijos simboliu

for i in range(5):  # For ciklas kartos kodą 5 kartus
    print(i)  # Išspausdins skaitiklį nuo 0 iki 4

# Kaip matote, skaitiklis prasideda nuo 0, o ne nuo 1
# Skaitiklis baigiasi vienetu mažesniu nei nurodyta riba
# Taip pat galime nurodyti pradinį skaitiklį
print("Pradinis skaitiklis 5:")
for i in range(5, 10):  # Skaitiklis prasidės nuo 5 ir baigsis 9
    print(i)  # Išspausdins skaitiklį nuo 5 iki 9

# Galime nurodyti ir žingsnį
print("Žingsnis 2:")
for i in range(0, 10, 2):  # Skaitiklis prasidės nuo 0 ir baigsis 8, žingsnis 2
    print(i)  # Išspausdins skaitiklį

# Naudojant funkciją range() galima nurodyti pradinį skaitiklį, galutinį skaitiklį ir žingsnį

# Jei nurodome tik vieną skaičių,jis bus laikomas galutiniu skaitikliu
# range(5) yra tas pats kas range(0, 5, 1) ir tas pats kas range(0, 5)
# Jis prasideda nuo 0 ir baigiasi 4
# 0, 1, 2, 3, 4

# Jei nurodome du skaičius, pirmas bus pradinis skaitiklis, o antras galutinis neįskaitant
# range(5, 10) yra tas pats kas range(5, 10, 1)
# Jis prasideda nuo 5 ir baigiasi 9
# 5, 6, 7, 8, 9

# Jei nurodome tris skaičius, pirmas bus pradinis skaitiklis, antras galutinis neįskaitant, o trečias žingsnis
# range(0, 10, 2) prasideda nuo 0 ir baigiasi 8, žingsnis 2
# 0, 2, 4, 6, 8

# Mes galime ir mažinti skaitiklį
print("Mažėjantis skaitiklis:")
for i in range(10, 0, -1):  # Skaitiklis prasidės nuo 10 ir baigsis 1, žingsnis -1
    print(i)  # Išspausdins skaitiklį nuo 10 iki 1

# Bet taip daryti negalima:
# for i in range(0, 10, -1):  # Skaitiklis prasidės nuo 0 ir baigsis 9, žingsnis -1
#    print(i)
# Nes skaitiklis prasidės nuo 0 ir bus mažėjantis, o ne didėjantis
# Ir taip mes gauname begalinį ciklą

# Galima naudoti for ciklą su if blokais
# Sekantis kodas paskaiciuos visų skaičių sumą nuo 0 iki 100 kurie dalinasi iš 3 arba 5

numbers_sum = 0  # Sukuriame kintamajį, kuriame saugosime sumą
for i in range(101):  # Einame per visus skaičius nuo 0 iki 100 imtinai
    if i % 3 == 0 or i % 5 == 0:  # Tikriname ar skaičius dalinasi iš 3 arba 5
        numbers_sum += i  # Jei taip, pridedame skaičių prie sumos
print("Suma:", numbers_sum)  # Išspausdiname sumą
