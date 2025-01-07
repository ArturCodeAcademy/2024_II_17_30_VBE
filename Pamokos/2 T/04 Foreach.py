# range funkcija generuoja skaiciu seka
# ir ciklas for pereina per ta seka
# kiekviena karta paimdamas sekančią reikšmę

# i - iteracijos kintamasis (iteratorius)
# range(5) - sugeneruoja seka nuo 0 iki 4
for i in range(5):
    print(i)
print()

# taip pat galima vietoj range funkcijos naudoti sąrašą
arr = [1, 2, 3, 4, 5]
# el - iteratorius į kurį patenka kiekvienas sąrašo elementas
for el in arr:
    print(el)
    # bet mes taip negalime pakeisti sąrašo elementų
    el = el * 10  # šis pakeitimas neveiks

# sąrašo elementai nepasikeitė
print(arr)  # [1, 2, 3, 4, 5]

# jei norime pakeisti sąrašo elementus, turime tai daryti pagal indeksą
for i in range(len(arr)):
    arr[i] = arr[i] * 10

print(arr)  # [10, 20, 30, 40, 50]

# Jei norime gauti ir indeksą ir elementą, galime naudoti enumerate funkciją
# kuri grąžina tuple (indeksas, elementas)
arr = [1, 2, 3, 4, 5]
# i - indeksas, el - elementas
for i, el in enumerate(arr):
    print(i, el)

# taip pat galime pakeisti sąrašo elementus
for i, el in enumerate(arr):
    arr[i] = el * 10
# sąrašo elementai pasikeitė
print(arr)  # [10, 20, 30, 40, 50]
