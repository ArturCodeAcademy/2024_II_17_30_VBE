# Parametrai gali turėti tokius pat pavadinimus,
# kaip ir kintamieji, kurie yra išorėje.

def print_nums_and_change_them(a, b):
    print(a, b)
    # Keičiame a ir b reikšmės
    # Tai nekeičia išorinių kintamųjų
    a = 10
    b = 20
    print(a, b)


a = 5
b = 10
print_nums_and_change_them(a, b)
# Galime matyti, kad funkcija pakeitė parametrų reikšmes,
# bet išoriniai kintamieji nepasikeitė
print(a, b)  # 5 10

# Jei mes norime naudoti išorinius kintamuosius funkcijoje
# ir neturime parametrų arba lokalių kintamųjų su tokiu pačiu pavadinimu,
# mes galime tai taip padaryti:
def print_nums():
    print(a, b)


print_nums()  # 5 10

# Bet jei mum reikia pakeisti išorinius kintamuosius,
# mes turime juos nurodyti kaip global
def change_nums():
    global a, b  # Nurodome, kad naudosime išorinius kintamuosius
    a = 10
    b = 20


print(a, b)  # 5 10
change_nums()
print(a, b)  # 10 20
