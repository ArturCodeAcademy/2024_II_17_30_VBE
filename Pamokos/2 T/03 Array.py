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

