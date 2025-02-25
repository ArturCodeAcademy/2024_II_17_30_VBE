# Prieš pradedant darbą su failais, reikia atidaryti norimą failą.
# Tai galima padaryti naudojant open() funkciją.

# open() funkcija turi dvi privalomas argumentus - failo pavadinimą ir atidarymo būdą.
# Atidarymo būdai:
# r - failas atidaromas skaitymui (default)

file = open("Text file.txt", "r")

# Atidarius failą, galima jį nuskaityti naudojant read() metodą.
# read() metodas nuskaito visą failą ir grąžina jį kaip vieną string'ą.
all_text = file.read()
print(all_text)
# Some text
# Second line
# Third line
# Last line

# Po nuskaitymo failą reikia uždaryti naudojant close() metodą.
file.close()

# Atidarius failą, galima jį nuskaityti eilutėmis naudojant readlines() metodą.
file = open("Text file.txt", "r")
lines = file.readlines()
print(lines)  # ['Some text\n', 'Second line\n', 'Third line\n', 'Last line']
file.close()

# Atidarius failą, galima jį nuskaityti eilutėmis naudojant readline() metodą.
file = open("Text file.txt", "r")
first_line = file.readline()
second_line = file.readline()
print(first_line)  # Some text\n
print(second_line)  # Second line\n
file.close()

# Taip pat galima nuskaityti failą naudojant for ciklą.
file = open("Text file.txt", "r")
for line in file:  # Iteruojame per visas failo eilutes
    print(line)
file.close()

# w - failas atidaromas rašymui.
# Jei failas neegzistuoja, jis sukurs naują.
# Jei failas egzistuoja, jis bus ištrintas ir sukurtas naujas.

file = open("Other file.txt", "w")
file.write("Hello, world!") # Į failą įrašomas tekstas
a = 10
b = 20
file.write(f"\n{a} + {b} = {a + b}")  # Į failą įrašomas tekstas
# Mes negalime į failą įrašyti skaičių ar kitų ne string'ų tipų,
# todėl prieš įrašant skaičių, jį reikia paversti į string'ą.
# file.write(a) # TypeError: write() argument must be str, not int
arr = [1, 2, 3, 4, 5]
file.write(f"\n{arr}")  # Į failą įrašomas tekstas
file.close()

# a - failas atidaromas rašymui.
# Jei failas egzistuoja, nauja informacija bus pridėta į pabaigą.
file = open("Other file.txt", "a")
file.write("\nThis is the end")  # Į failą įrašomas tekstas
file.close()

# x - failas atidaromas rašymui.
# Jei failas egzistuoja, bus išmestas klaidos pranešimas.
# file = open("Other file.txt", "x")  # FileExistsError: [Errno 17] File exists: 'Other file.txt'
file = open("New file.txt", "x")
file.write("New file")
file.close()

# Mes galime pamiršti uždaryti failą
# Dėl to gali kilti problemų.
# Geriausias būdas uždaryti failą yra naudojant with bloką.

with open("Text file.txt", "r") as file:
    all_text = file.read()
    print(all_text)
    # Some text
    # Second line
    # Third line
    # Last line

# Kai mes naudojame with bloką, mes nesame priversti uždaryti failo.
# with blokas uždaro failą automatiškai, kai jis baigiasi.

with open("Text file.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # ['Some text\n', 'Second line\n', 'Third line\n', 'Last line']

with open("Other file.txt", "w") as file:
    file.write("Hello, world!")  # Į failą įrašomas tekstas
    a = 10
    b = 20
    file.write(f"\n{a} + {b} = {a + b}")  # Į failą įrašomas tekstas
    arr = [1, 2, 3, 4, 5]
    file.write(f"\n{arr}")  # Į failą įrašomas tekstas

# Mes negalime rašyti į failą ne string'ų tipų.
# Norint įrašyti skaičių, jį reikia paversti į string'ą.
data = 10
with open("Other file.txt", "a") as file:
    file.write(str(data))  # data konvertuojamas į string'ą
    file.write(f"{data}")  # data konvertuojamas į string'ą
    file.write(data)  # TypeError: write() argument must be str, not int
