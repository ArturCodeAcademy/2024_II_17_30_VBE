# Jei mes iš anksto nežinome kiek reikšmių bus
# Arba reikšmių bus daug ir jas saugoti kintamuosiuose nėra prasmės
# Tuomet naudojame masyvus
# Masyvas yra objektas, kuris saugo daug reikšmių

# Masyvas sukuriamas naudojant kvadratinius skliaustus
arr = []  # Sukuriamas tuščias masyvas, kuris neturi jokių reikšmių
arr = list()  # Tas pats kas arr = []
print(arr)  # []

arr = [1, 2, 3, 4, 5]  # Sukuriamas masyvas su 5 reikšmėmis
print(arr)  # [1, 2, 3, 4, 5]

# Masyve gali būti saugomos bet kokios reikšmės
arr = [1, 'a', True, 2.5]
print(arr)  # [1, 'a', True, 2.5]

# Jei norime pasiekti masyvo reikšmę, tai naudojame indeksavimą
# Indeksavimas yra būdas pasiekti masyvo elementą
# Indeksavimas atrodo taip: masyvas[indeksas]
# Indeksavimas prasideda nuo 0, tai yra pirmas elementas yra 0, antras 1 ir t.t.
arr = [1, 2, 3, 4, 5]
print(arr[0])  # 1

# Jei norime pakeisti masyvo reikšmę, tai taip pat naudojame indeksavimą
arr[0] = 10  # Pakeičiame pirmą masyvo elementą į 10
print(arr)  # [10, 2, 3, 4, 5]

# Masyvo ilgį galime gauti naudojant len() funkciją
arr = [1, 2, 3, 4, 5]
print(len(arr))  # 5 - masyvo ilgis (kiek elementų yra masyve)

# Taipat galime naudoti neigiamus indeksus
# Neigiamas indeksas prasideda nuo -1. Paskutinis elementas yra -1, antras nuo galo -2 ir t.t.
arr = [1, 2, 3, 4, 5]
print(arr[-1])  # 5 - paskutinis masyvo elementas
print(arr[-2])  # 4 - antras nuo galo masyvo elementas

# Iteruoti per masyvą galime naudojant for ciklą
# Iteravimas yra būdas pereiti per visus masyvo elementus
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)):  # range(len(arr)) - sukuriame skaičių seką nuo 0 iki masyvo ilgio
    print(arr[i])  # Spausdiname masyvo elementą

# Tuščią masyvą galime sukurti naudojant list() funkciją
arr = list()  # tas pats kas arr = []
print(arr)  # []

# Kartais reikia atlikti operacijas su masyvais.
# Pavyzdžiui, pridėti papildomą elementą į masyvą,
# ištrinti elementą iš masyvo, surasti elementą masyve ir t.t.

arr = [1, 2, 3, 4, 5]
print(arr)  # [1, 2, 3, 4, 5]

# Pridėti elementą į masyvą galime naudojant append() metodą

arr.append(6)  # Pridedame elementą 6 į masyvą
print(arr)  # [1, 2, 3, 4, 5, 6]

# Ištrinti elementą iš masyvo galime naudojant remove() metodą
arr.remove(3)  # Ištriname elementą 3 iš masyvo
print(arr)  # [1, 2, 4, 5, 6]

# Surasti elementą masyve galime naudojant index() metodą
print(arr.index(4))  # 2 - elementas 4 yra antroje pozicijoje

# Panaikinti elementą iš masyvo pagal indeksą galime naudojant pop() metodą
arr.pop(2)  # Panaikiname elementą 4 iš masyvo
print(arr)  # [1, 2, 5, 6]

# Prideti elementą pagal indeksą galime naudojant insert() metodą
arr.insert(2, 10)  # Pridedame elementą 4 į masyvą antroje pozicijoje
print(arr)  # [1, 2, 10, 5, 6]

# Surikiuoti masyvą galime naudojant sort() metodą
arr.sort()  # Surikiuojame masyvą
print(arr)  # [1, 2, 5, 6, 10]

# Atvirkštinę masyvo tvarką galime gauti naudojant reverse() metodą
arr.reverse()  # Apverčiame masyvą
print(arr)  # [10, 6, 5, 2, 1]

# Pridėti kitą masyvą galime naudojant extend() metodą
arr2 = [7, 8, 9]
arr.extend(arr2)  # Pridedame masyvą arr2 į masyvą arr
print(arr)  # [10, 6, 5, 2, 1, 7, 8, 9]

# Taip pat galime naudoti + operatorių
# Tai sujungs du masyvus į vieną
arr3 = [11, 12, 13]
print(arr2 + arr3)  # [7, 8, 9, 11, 12, 13]

# Prie dabartinio masyvo galime pridėti kitą masyvą naudojant +=
arr += arr3  # Pridedame masyvą arr3 prie masyvo arr
print(arr)  # [10, 6, 5, 2, 1, 7, 8, 9, 11, 12, 13]

# Taip pat galime naudoti * operatorių
# Tai pakartos masyvą nurodytą skaičių kartų
print(arr2 * 3)  # [7, 8, 9, 7, 8, 9, 7, 8, 9]

# Išvalyti masyvą galime naudojant clear() metodą
arr.clear()  # Išvalome masyvą
print(arr)  # []
