# Kintamieji tai atminties vieta, kurioje saugomi duomenys.
# Kintamieji turi pavadinimą, reikšmę ir tipą.

# Kintamųjų tipai:
# int - sveikasis skaičius
# float - skaičius su kableliu / realus skaičius
# str - tekstas
# bool - loginis kintamasis (True / False)

# Jei mes norime sukurti kintamąjį,
# tai mes tiesiog parašome jo pavadinimą ir priskiriame reikšmę.

# Kintamųjų pavadinimai:
# Kintamieji gali būti sudaryti iš raidžių, skaičių ir _ simbolio.
# Kintamieji negali prasidėti skaičiumi.
# Kintamieji negali būti pavadinimai, kurie yra rezervuoti programavimo kalbos (if, else, while, for, ...).
# Kintamieji gali būti jautrūs didžiosioms ir mažosioms raidėms. (pvz. kintamasis ir Kintamasis yra skirtingi kintamieji)

# Kintamųjų priskyrimas:
a = 5
print(a)  # 5

# Matematinių operacijų naudojimas su kintamaisiais:

# Sudėtis
b = 10
c = a + b
print(c)  # 15

# Atimtis
d = a - b
print(d)  # -5

# Daugyba
e = a * b
print(e)  # 50

# Dalyba
f = a / b
print(f)  # 0.5

# Liekana
a = 4
b = 10
g = b % a
print(g)  # 2

# Sveikųjų skaičių dalyba
h1 = b / a
h2 = b // a  # sveikųjų skaičių dalyba, atmetam viska po kablelio
print(h1)  # 2.5
print(h2)  # 2

# Laipsnio kelimas
i = 2 ** 10  # 2 pakeliamas laipsniu 10
print(i)  # 1024

# Sveikas skaicius
integer_number = 5

# Realus skaicius
float_number = 5.5

# Tekstas
text = "Hello, World!"

# Logine reiksme
logical = True

# Išvedame kintamuosius
print(integer_number)
print(float_number)
print(text)
print(logical)
