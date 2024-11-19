# Kartais mum reikia praleisti kai kurią iteraciją ir tęsti kitą.
# Tai galime padaryti naudodami continue.
# Šis operatorius praleidžia visą likusį ciklo bloką ir pradeda naują iteraciją.

# Pavyzdžiui, jei norime išvesti visus nelyginius skaičius nuo 1 iki 10, galime naudoti continue:

for i in range(1, 11):
    if i % 2 == 0:
        continue  # Praleidžiame visą likusį ciklo bloką ir pradedame naują iteraciją
    print(i)

# Rezultatas: 1 3 5 7 9

# continue veikia su visais ciklais: for, while

# Atitinkamas pavyzdys su while ciklu:

i = 1
while i < 11:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# continue veikia tik su ciklais, todėl jį negalima naudoti be ciklo.

# Venkite tokių continue be sąlygos, nes jie nėra naudingi ir gali sukelti klaidų.
i = 1
while i < 11:
    i += 1
    continue
    print("Šis tekstas niekada nebus išvestas")

for i in range(10):
    continue
    print("Šis tekstas niekada nebus išvestas")

# Jei mes norime sustabdyti ciklą, galime naudoti break operatorių.
# Šis operatorius sustabdo ciklą ir išeina iš jo.

# Pavyzdžiui, jei norime išvesti visus skaičius nuo 1 iki 10,
# bet sustabdyti ciklą, kai pasiekiame 5, galime naudoti break:

for i in range(1, 11):
    print(i)
    if i == 5:
        break  # Sustabdome ciklą

# Rezultatas: 1 2 3 4 5

# break veikia su visais ciklais: for, while

# Atitinkamas pavyzdys su while ciklu:

i = 1
while i < 11:
    print(i)
    if i == 5:
        break  # Sustabdome ciklą
    i += 1

# Rezultatas: 1 2 3 4 5

# break veikia tik su ciklais, todėl jį negalima naudoti be ciklo.

# Tokie ciklai nei karto nesuveiks:

while True:
    break
    print("Šis tekstas niekada nebus išvestas")

for i in range(10):
    break
    print("Šis tekstas niekada nebus išvestas")