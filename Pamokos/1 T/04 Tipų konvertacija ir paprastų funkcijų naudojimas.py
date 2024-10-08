# Taikant funkciją str() galima konvertuoti bet kokį kintamąjį į tekstą.

integer_number = 10  # Sukuriamas sveikas skaičius
number_as_string = str(integer_number)  # Sveikas skaičius konvertuojamas į tekstą

# Sveikas skaičius pridedamas prie sveiko skaičiaus
print(integer_number + integer_number)  # 20
# Tekstas pridedamas prie teksto
print(number_as_string + number_as_string)  # 1010
# Sveiką skaičių prideti prie teksto negalima
# Galite atkomentuoti sekančią eilutę ir pamatyti klaidą
# print(integer_number + number_as_string)


real_number = 10.5  # Sukuriamas realus skaičius
number_as_string = str(real_number)  # Realus skaičius konvertuojamas į tekstą


logical_value = True  # Sukuriamas loginis kintamasis
logical_value_as_string = str(logical_value)  # Loginis kintamasis konvertuojamas į tekstą

print(logical_value)  # True
print(logical_value_as_string)  # True

# Taikant funkciją int() galima konvertuoti kai kurius tipus į sveikąjį skaičių.

# Sukuriamas tekstas
text = "10"
# Tekstas konvertuojamas į sveikąjį skaičių
number = int(text)

# Sveikas skaičius pridedamas prie sveiko skaičiaus
print(number + number)  # 20
# Tekstas pridedamas prie teksto
print(text + text)  # 1010

# Tekstas, kuris nėra skaičius, negali būti konvertuotas į sveikąjį skaičių.
text = "tekstas kuris nėra skaičius"
# Galite atkomentuoti sekančią eilutę ir pamatyti klaidą
# number = int(text)

# Taip pat galima konvertuoti realųjį skaičių į sveikąjį skaičių.
# Sukuriamas realus skaičius
real_number = 10.5
# Realus skaičius konvertuojamas į sveikąjį skaičių
# Konvertuojant realųjį skaičių į sveikąjį, skaičiai po kablelio yra atmetami.
number = int(real_number)
print(number)  # 10


# Taip pat galima konvertuoti loginį kintamąjį į sveikąjį skaičių.
# Sukuriamas loginis kintamasis
logical_value = True
# Loginis kintamasis konvertuojamas į sveikąjį skaičių
# True konvertuojamas į 1, o False į 0.
number = int(logical_value)
print(number)  # 1

# Taip pat galima konvertuoti skaičių iš šešioliktainės į dešimtainę skaičių sistemą.
# Sukuriamas šešioliktainis skaičius
hex_number = "A"
# Šešioliktainis skaičius konvertuojamas į dešimtainį skaičių
number = int(hex_number, 16)  # 16 nurodo, kad skaičius yra šešioliktainis
print(number)  # 10

# Taip pat galima konvertuoti skaičių iš dvejetainės į dešimtainę skaičių sistemą.
# Sukuriamas dvejetainis skaičius
binary_number = "1010"
# Dvejetainis skaičius konvertuojamas į dešimtainį skaičių
number = int(binary_number, 2)  # 2 nurodo, kad skaičius yra dvejetainis
print(number)  # 10

# Decimal binary hexadecimal
# 0       0      0
# 1       1      1
# 2       10     2
# 3       11     3
# 4       100    4
# 5       101    5
# 6       110    6
# 7       111    7
# 8       1000   8
# 9       1001   9
# 10      1010   A
# 11      1011   B
# 12      1100   C
# 13      1101   D
# 14      1110   E
# 15      1111   F
# 16      10000  10


# Taikant funkciją float() galima konvertuoti kai kurius tipus į realųjį skaičių.

# Sukuriamas tekstas
text = "10.5"
# Tekstas konvertuojamas į realųjį skaičių
real_number = float(text)
# Atspausdinamas realus skaičius
print(real_number)  # 10.5

# Sukuriamas sveikas skaičius
integer_number = 10
# Sveikas skaičius konvertuojamas į realųjį skaičių
real_number = float(integer_number)
# Atspausdinamas realus skaičius
print(real_number)  # 10.0

# Sukuriamas loginis kintamasis
logical_value = True
# Loginis kintamasis konvertuojamas į realųjį skaičių
# True konvertuojamas į 1.0, o False į 0.0
real_number = float(logical_value)
# Atspausdinamas realus skaičius
print(real_number)  # 1.0

# Sukuriamas tekstas
text = "tekstas kuris nera skaicius"
# Tekstas konvertuojamas į realųjį skaičių
# Jei tekstas nėra skaičius, bus iškviesta klaida
# Galite atkomentuoti sekančią eilutę ir pamatyti klaidą
# real_number = float(text)
