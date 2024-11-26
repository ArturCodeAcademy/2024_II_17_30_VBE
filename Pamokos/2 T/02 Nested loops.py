# Jei mum reikia kartoti operaciją kurią kartoja kažkius veiksmus, galime naudoti ciklą cikle.

# Pavyzdys: Daugybos lentelė

print("Daugybos lentelė")
print("   |  1  2  3  4  5  6  7  8  9")
print("---+---------------------------")
for i in range(1, 10):
    print(f"{i}  |", end=" ")
    for j in range(1, 10):  # iteratoriai turi būti skirtingi, nes kitaip jie perrašys vienas kitą
        print(f"{i * j:2}", end=" ")
    print()

# Tai gali būti ir while ciklas
# Arba kombinacija for ir while ciklų

print("\nDaugybos lentelė")
print("   |  1  2  3  4  5  6  7  8  9")
print("---+---------------------------")
for i in range(1, 10):
    j = 1
    print(f"{i}  |", end=" ")
    while j < 10:
        print(f"{i * j:2}", end=" ")
        j += 1
    print()

# Dar vienas pavyzdys: išvesti visus pirminius skaičius iki 100

print("\nPirminiai skaičiai iki 100:")
for i in range(2, 101):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:  # Jei skaičius dalijasi iš kito skaičiaus be liekanos, jis nėra pirminis
            is_prime = False
            break

    if is_prime:
        print(i, end=" ")

# Operatoriai continue ir break kurie naudojami vidiniame cikle,
# neitakoja išorinio ciklo. Jei norime sustabdyti išorinį ciklą, turime naudoti papildomą kintamąjį.

for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 20:
            break  # Šis break veikia tik su vidiniu ciklu
            break  # Šis break net neveiks, nes jis yra po kito break
        print(f"{i} * {j} = {i * j}")
    print()


# Pavyzdys su papildomu kintamuoju:

stop = False
for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 20:
            stop = True  # Nustatome papildomą kintamąjį
            break  # Šis break veikia tik su vidiniu ciklu
        print(f"{i} * {j} = {i * j}")
    if stop:  # Tikriname papildomą kintamąjį
        break  # Šis break veikia su išoriniu ciklu
    print()


# Taip pat ciklai turi else bloką, kuris įvykdomas tik tada, kai ciklas baigiasi be break.

for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 20:
            break
        print(f"{i} * {j} = {i * j}")
    else:
        print("Vidinis ciklas baigtas be break")
    print()


i = 1

while i < 10:
    j = 1
    while j < 10:
        if i * j > 20:
            break
        print(f"{i} * {j} = {i * j}")
        j += 1
    else:
        print("Vidinis ciklas baigtas be break")
    i += 1
    print()


# Žinant tą informacija, galime pakeisti pavyzdį su pirminiais skaičiais iki 100:

print("\nPirminiai skaičiai iki 100:")
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:  # Jei skaičius dalijasi iš kito skaičiaus be liekanos, jis nėra pirminis
            break  # Šis break veikia tik su vidiniu ciklu
    else:  # Šis else bus įvykdomas tik tada, kai vidinis ciklas baigsis be break
        print(i, end=" ")