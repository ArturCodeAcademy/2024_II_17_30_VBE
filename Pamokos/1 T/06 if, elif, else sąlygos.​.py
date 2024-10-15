condition = False

# Mes galime palyginti du skaičius naudodami lygybės operatorius.
a = 10
b = 20

# == operatorius tikrina ar du skaičiai yra lygūs
print(a == b)  # False

# != operatorius tikrina ar du skaičiai nėra lygūs
print(a != b)  # True

# > operatorius tikrina ar pirmas skaičius yra didesnis už antrąjį
print(a > b)  # False

# < operatorius tikrina ar pirmas skaičius yra mažesnis už antrąjį
print(a < b)  # True

# >= operatorius tikrina ar pirmas skaičius yra didesnis arba lygus antrajam
print(a >= b)  # False

# <= operatorius tikrina ar pirmas skaičius yra mažesnis arba lygus antrajam
print(a <= b)  # True

# Palyginimo operatoriai gali būti naudojami su tekstu
text1 = "Hello"
text2 = "World"

print(text1 == text2)  # False
print(text1 != text2)  # True

# Palyginimas veikia pagal ASCII lentelę
# ASCII lentelė: https://www.ascii-code.com/
# Kiekvienas simbolis turi savo ASCII reikšmę
# Palyginimas veikia taip, kad palyginami simbolių ASCII kodai
# Jei pirmo simbolio ASCII kodas didesnis, tai ir pirmas tekstas didesnis
print(text1 > text2)  # False
print(text1 < text2)  # True
print(text1 >= text2)  # False
print(text1 <= text2)  # True

# Palyginimo operatoriai gali būti naudojami su loginiais kintamaisiais
logical1 = True
logical2 = False

print(logical1 == logical2)  # False
print(logical1 != logical2)  # True

# Taip pat galima palyginti loginius kintamuosius
# Bet geriau naudoti tik == ir !=
print(logical1 > logical2)  # True
print(logical1 < logical2)  # False
print(logical1 >= logical2)  # True
print(logical1 <= logical2)  # False

# Kai mes turime kelias sąlygas,
# galime jas sujungti naudodami loginius operatorius.

# and operatorius reiškia, kad visos sąlygos turi būti tiesos
# Jei nors viena sąlyga netiesa, sąlyga bus netiesa
# Jei visos sąlygos tiesos, sąlyga bus tiesa
print("and operator")
print("True and True:", True and True)  # True
print("True and False:", True and False)  # False
print("False and True:", False and True)  # False
print("False and False:", False and False, "\n")  # False

# or operatorius reiškia, kad bent viena sąlyga turi būti tiesa
# Jei bent viena sąlyga tiesa, sąlyga bus tiesa
# Jei visos sąlygos netiesos, sąlyga bus netiesa
print("or operator")
print("True or True:", True or True)  # True
print("True or False:", True or False)  # True
print("False or True:", False or True)  # True
print("False or False:", False or False, "\n")  # False

# not operatorius pakeičia sąlygos rezultatą
# Jei sąlyga yra tiesa, not pakeis ją į netiesą
# Jei sąlyga yra netiesa, not pakeis ją į tiesą
print("not operator")
print("not True:", not True)  # False
print("not False:", not False)  # True

# and ir or operatoriai gali būti sujungti
print("and ir or operatoriai")
print("True and True or False:", True and True or False)  # True

# and turi didesnį prioritetą už or
# jei norime pakeisti prioritetą, galime naudoti skliaustus
# Čia pirmiausia bus tikrinama False or True, tada True and ...
print("True and (True or False):", True and (True or False))  # True
# Čia pirmiausia bus tikrinama True and False, tada ... or True
print("True and False or True:", True and False or True)  # True

# Junginiai gali būti sudėtingesni
print("Sudėtingesnis junginys")
print("True and (True or False) and (False or not True):", True and (True or False) and (False or not True)) # False

# Vietoj True ir False galime naudoti kitus kintamuosius arbą sąlygas
a = 10
b = 20
c = 30
d = 40

# Jei a yra didesnis už b ir c yra mažesnis už d, sąlyga bus tiesa
print("a > b and c < d:", a > b and c < d)  # False

# Jei c yra didžiausias skaičius, sąlyga bus tiesa
print("c > a and c > b and c > d:", c > a and c > b and c > d)  # False

# Kai mum reikia atlikti veiksmus, kai sąlyga yra tiesa, galime naudoti if bloką.

# Jei sąlyga yra tiesa, vykdomas kodas, kuris yra įdėtas į if bloką.
# Įdėti kodą į if bloką reikia atskirti tabuliacijos simboliu.

# Pavyzdžiui:
a = 10
b = 20

print("a:", a)
print("b:", b)
if a < b: # Jei a yra mažesnis už b, vykdomas kodas, kuris yra įdėtas į if bloką
    print("a yra mažesnis už b")

# Į if bloką galime įdėti daugiau kodo
if a < b:
    print("a yra mažesnis už b")
    print("a:", a)
    print("b:", b)
    print("a + b:", a + b)
    print("a - b:", a - b)
    print("a * b:", a * b)
    print("a / b:", a / b)

# Jei sąlyga yra netiesa, kodas, kuris yra įdėtas į if bloką, nevykdomas
if a > b:
    print("a yra didesnis už b")  # Šis kodas nevykdomas, nes a nėra didesnis už b

# Jei norime, kad kodas būtų vykdomas, kai sąlyga yra netiesa, galime naudoti else bloką
if a > b:
    print("a yra didesnis už b")
else:
    print("a nėra didesnis už b")

# Else blokas gali būti naudojamas tik su if bloku
# Else blokas turi būti po if bloko arba po visų elif blokų
# Else blokas gali būti tik vienas

# Jei turime kelias sąlygas, galime naudoti elif bloką
# Elif blokas reiškia "kitu atveju"
# Jei if sąlyga yra netiesa, tikrinama elif sąlyga
# Jei elif sąlyga yra tiesa, vykdomas elif blokas
# Jei elif sąlyga yra netiesa, vykdomas else blokas

# Pavyzdžiui:
a = 10
b = 20

print("a:", a)
print("b:", b)

if a > b: # Jei a yra didesnis už b, vykdomas kodas, kuris yra įd
    print("a yra didesnis už b")
else:
    if a < b: # Jei a yra mažesnis už b, vykdomas kodas, kuris yra įdėtas į elif bloką
        print("a yra mažesnis už b")
    else: # Jei a nėra didesnis už b ir nėra mažesnis už b, vykdomas kodas, kuris yra įdėtas į else bloką
        print("a yra lygus b")

if a > b: # Jei a yra didesnis už b, vykdomas kodas, kuris yra įd
    print("a yra didesnis už b")
elif a < b: # Jei a yra mažesnis už b, vykdomas kodas, kuris yra įdėtas į elif bloką
    print("a yra mažesnis už b")
else: # Jei a nėra didesnis už b ir nėra mažesnis už b, vykdomas kodas, kuris yra įdėtas į else bloką
    print("a yra lygus b")

# Elif blokų gali būti kiek norime
a = 5

if a == 1:
    print("a yra 1")
elif a == 2:
    print("a yra 2")
elif a == 3:
    print("a yra 3")
elif a == 4:
    print("a yra 4")
elif a == 5:
    print("a yra 5")
else:
    print("a nėra 1, 2, 3, 4 arba 5")

# if blokas gali būti įdėtas į kitą if bloką

a = 100
b = 20
c = 30

if a < b:
    print("a yra mažesnis už b")
    if b < c:
        print("b yra mažesnis už c")
    else:
        print("b nėra mažesnis už c")
else:
    print("a nėra mažesnis už b")
    if b < c:
        print("b yra mažesnis už c")
    else:
        print("b nėra mažesnis už c")

print("Pabaiga")