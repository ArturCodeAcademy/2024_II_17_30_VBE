# Kuriame kintamuosius ir atliekame paprastus veiksmus su jais
a = 5
b = 3

# Sudėtis
sum_of_nums = a + b
print(sum_of_nums)  # 8

# Atimtis
subtraction_of_nums = a - b
print(subtraction_of_nums)  # 2

# Daugyba
multiplication_of_nums = a * b
print(multiplication_of_nums)  # 15

# Dalyba
division_of_nums = a / b
print(division_of_nums)  # 1.6666666666666667

# Dalyba be liekanos
# Atmetame viską po kablelio
division_without_remainder_of_nums = a // b
print(division_without_remainder_of_nums)  # 1

# Liekana
# Rezultatas yra 2, nes 5 / 3 = 1 ir liekana 2
remainder_of_nums = a % b
print(remainder_of_nums)  # 2

# Kėlimas laipsniu
# a pakeliamas b laipsniu
exponentiation_of_nums = a ** b
print(exponentiation_of_nums)  # 125

a = 2
b = 3

# Skliausteliai () turi didesnį prioritetą nei bet kokie kiti operatoriai
# Todėl pirmiausia bus atliekami veiksmai skliausteliuose
result = (a + b) * a
print(result)  # 10 -> (2 + 3) * 2 = 10 -> 5 * 2 = 10

# Taip pat galime naudoti daugiau skliaustelių
result = ((a + b) * (a - b)) ** b
"""
((2 + 3) * (2 - 3)) ** 3
(5 * (-1)) ** 3
(-5) ** 3
125
"""
print(result)  # 125


# Mes galime atlikti operacijas su kintamaisiais
# ir priskirti rezultatą kintamajam iškart.
var = 5

# Prie kintamojo pridedame 1 ir rezultatą priskiriame tam pačiam kintamajam
var = var + 1
print(var)  # 6

# Ta pati operacija, bet trumpesnė forma
var += 10
print(var)  # 16

# Taip pat galime atimti, dauginti, dalinti ir kt.
var -= 1
print(var)  # 15

var *= 2
print(var)  # 30

var //= 7
print(var)  # 4

var %= 3
print(var)  # 1

var /= 2
print(var)  # 0.5

var **= 3
print(var)  # 0.125