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


# Tam, kad nukopijuoti masyvą, butinai reikia naudoti copy() metodą
# Jei mes tiesiog priskirsime masyvą kintamajam, tai kintamasis rodis į tą patį masyvą

arr = [1, 2, 3, 4, 5]
arr2 = arr  # arr2 rodo į tą patį masyvą kaip ir arr

arr2[0] = 10  # Pakeičiame arr2 pirmą elementą į 10

# Nors pakeitėme arr2, bet pakeitimas paveikė ir arr
# Nes abu kintamieji rodo į tą patį masyvą
print(arr)  # [10, 2, 3, 4, 5]
print(arr2)  # [10, 2, 3, 4, 5]

# Norint nukopijuoti masyvą, reikia naudoti copy() metodą
arr = [1, 2, 3, 4, 5]
arr2 = arr.copy()  # arr2 dabar rodo į naują masyvą, kuris yra kopija arr

arr2[0] = 10  # Pakeičiame arr2 pirmą elementą į 10

# Pakeitimas paveikė tik arr2, nes arr2 yra kopija arr
print(arr)  # [1, 2, 3, 4, 5]
print(arr2)  # [10, 2, 3, 4, 5]

# Taip pat galime naudoti slice operatorių
arr = [1, 2, 3, 4, 5]
arr2 = arr[:]  # arr2 dabar rodo į naują masyvą, kuris yra kopija arr

arr2[0] = 10  # Pakeičiame arr2 pirmą elementą į 10

# Pakeitimas paveikė tik arr2, nes arr2 yra kopija arr
print(arr)  # [1, 2, 3, 4, 5]
print(arr2)  # [10, 2, 3, 4, 5]

# Taip pat galime naudoti list() funkciją
arr = [1, 2, 3, 4, 5]
arr2 = list(arr)  # arr2 dabar rodo į naują masyvą, kuris yra kopija arr

arr2[0] = 10  # Pakeičiame arr2 pirmą elementą į 10

# Pakeitimas paveikė tik arr2, nes arr2 yra kopija arr
print(arr)  # [1, 2, 3, 4, 5]

# Tai galime naudoti bet kurią iš šių trijų galimybių
# (copy(), slice operatorius, list() funkciją)

# Naudojant slice operatorių galime nukopijuoti tik dalį masyvo
arr = [1, 2, 3, 4, 5]
arr2 = arr[1:4]  # Kopijuojame masyvo dalį nuo indekso 1 iki 4

# [from:to] - nuo indekso from iki indekso to
# from - įskaitant, to - neįskaitant
print(arr2)  # [2, 3, 4]

# Taipat galime nurodyti tik vieną indeksą
# Tuomet bus kopijuojama nuo nurodyto indekso iki galo
arr = [1, 2, 3, 4, 5]
arr2 = arr[2:]  # Kopijuojame masyvo dalį nuo indekso 2 iki galo
print(arr2)  # [3, 4, 5]

# Arba nuo pradžios iki nurodyto indekso
arr = [1, 2, 3, 4, 5]
arr2 = arr[:3]  # Kopijuojame masyvo dalį nuo pradžios iki indekso 3
print(arr2)  # [1, 2, 3]

# Taip pat galime nurodyti trečią parametrą, kuris nurodo žingsnį
# Žingsnis nurodo kas kiek elementų kopijuoti
arr = [1, 2, 3, 4, 5]
arr2 = arr[::2]  # Kopijuojame kas antrą elementą, pradedant nuo pradžios iki galo
print(arr2)  # [1, 3, 5]

# Taip pat galime nurodyti neigiamą žingsnį
arr = [1, 2, 3, 4, 5]
arr2 = arr[::-1]  # Kopijuojame masyvą atvirkštine tvarka
print(arr2)  # [5, 4, 3, 2, 1]

# Parašysime visus slice operatoriaus argumentus
# arr[from:to:step]
# from - nuo kurio indekso kopijuoti
# to - iki kurio indekso kopijuoti
# step - kas kiek elementų kopijuoti
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = arr[1:8:2]  # Kopijuojame kas antrą elementą nuo indekso 1 iki 8
print(arr2)  # [2, 4, 6, 8]
arr3 = arr[-1:-8:-2]  # Kopijuojame kas antrą elementą nuo paskutinio iki -8
print(arr3)  # [10, 8, 6, 4]

# Masyvas iš range() funkcijos
# 0 - 100
# range() funkcija sukuria skaičių seką
# list() funkcija paverčia skaičių seką į masyvą
arr = list(range(101))
print(arr)

# Naudojant funkciją list() kartu su range() galime sukurti masyvą.

# Sukursime masyvą, kuris bus nuo 1 iki 10
arr = list(range(1, 11))
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sukursime masyvą, kuris bus nuo 1 iki 10, bet kas antrą elementą
arr = list(range(1, 11, 2))
print(arr)  # [1, 3, 5, 7, 9]

# Sukursime masyvą, kuris bus nuo 10 iki 1
arr = list(range(10, 0, -1))
print(arr)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Viskas veikia taip pat kaip ir su for ciklu
# Tik šiuo atveju mes kuriame masyvą


# Jei norime sukurti masyvą iš įvestos eilutės, tai galime naudoti split() metodą,
# kuris padalins eilutę į atskirus elementus pagal nurodytą simbolį.

# line = input() # atkomentuokite, jei norite patis įvesti eilutę
line = "1 2 3 4 5 6 7 8 9 10"  # užkomentuokite, jei norite patis įvesti eilutę
str_array = line.split()  # padaliname eilutę pagal tarpus
print(str_array)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# Mes gavome masyvą, kurio elementai yra tekstai. Norint gauti skaičius, reikia juos sukonvertuoti.
arr = list(map(int, str_array))  # sukonvertuojame tekstus į skaičius
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Jei norime sukonvertuoti į float, tai galime naudoti float vietoj int.
arr = list(map(float, str_array))  # sukonvertuojame tekstus į skaičius
print(arr)  # [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

line = "1,2,3,4,5,6,7,8,9,10"  # užkomentuokite, jei norite patis įvesti eilutę
str_array = line.split(",")  # padaliname eilutę pagal kablelį
print(str_array)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

line = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"  # užkomentuokite, jei norite patis įvesti eilutę
str_array = line.split(", ")  # padaliname eilutę pagal kablelį ir tarpą
print(str_array)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Funkcijos veikiančios su masyvais
arr = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, -5, 6, 7, 8, 9, 10]

# min() - mažiausia reikšmė masyve
print(min(arr))  # -5

# max() - didžiausia reikšmė masyve
print(max(arr))  # 10

# sum() - sumuoja visus masyvo elementus
print(sum(arr))  # 40

# index() - grąžina pirmo sutampančio elemento indeksą
print(arr.index(-5))  # 5

# sorted() - sukurs naują masyvą, kuris bus surikiuotas
sorted_arr = sorted(arr)
print(sorted_arr)  # [-5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)  # [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, -5, 6, 7, 8, 9, 10]

# sort
arr.sort()  # surikiuoja masyvą
print(arr)  # [-5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]