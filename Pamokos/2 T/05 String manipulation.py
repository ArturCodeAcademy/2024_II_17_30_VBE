# Jei mes norime sukurti teksto kintamąjį,
# galime naudoti '' arba "" kabutes.
text = "Hello, World!"
print(text)

text = 'Hello, World!'
print(text)

# jei tekstas turi būti sudarytas iš kelių eilučių,
# mes galime naudoti trijų kabučių simbolį
text = """Hello,
World!"""
print(text)

text = '''Hello,
World!'''
print(text)

# Jei mes norime bet kokią reikšmę sukonvertuoti į tekstą,
# mes galime naudoti str() funkciją.

arr = [1, 2, 3, 4, 5]
num = 10
real = 3.14
logic = True

# str() funkcija konvertuoja bet kokią reikšmę į tekstą
arr_str = str(arr)
num_str = str(num)
real_str = str(real)
logic_str = str(logic)

# ir dabar mes galime sujungti tekstus
result = arr_str + " " + num_str + " " + real_str + " " + logic_str
print(result)

# jei tai darome be str() funkcijos, gausime TypeError
# nes tekstas negali būti sujungtas su kitomis reikšmėmis
# result = arr + " " + num + " " + real + " " + logic
# print(result)

# Taip pat teksto sujungimui galime naudoti f string
# f string yra naujas būdas sujungti tekstą su kitomis reikšmėmis
# naudojant { } skliaustus
result = f"{arr} {num} {real} {logic}"
print(result)

# f string leidžia naudoti bet kokias reikšmes
# ir jas formatuoti
result = f"{arr} {num} {real:.5f} {logic}"
print(result)

# f string leidžia naudoti bet kokias išraiškas
# ir jas formatuoti

# float formatavimas
# po kablelio skaičių kiekis
print(f"{3.141592653589793:.5f}")  # 3.14159
print(f"{3.141592653589793:.2f}")  # 3.14
print(f"{3.141592653589793:.0f}")  # 3

# sveikųjų skaičių formatavimas
# skaičių kiekis
print(f"{12345:10}")  #      12345
print(f"{12345:5}")  # 12345
print(f"{12345:1}")  # 12345

# skaičių formatavimas su tūkstančių skirtuku
print(f"{123456789:,.0f}")  # 123,456,789
print(f"{123456789:,.2f}")  # 123,456,789.00

# skaičių formatavimas su ju stumimu į dešinę
print(f"{12345:>10} Kitas tekstas")  #      12345 Kitas tekstas
print(f"{12345:>5} Kitas tekstas")  # 12345 Kitas tekst
print(f"{12345:>1} Kitas tekstas")  # 12345 Kitas tekst

# skaičių formatavimas su ju stumimu į kairę
print(f"{12345:<10} Kitas tekstas")  # 12345      Kitas tekstas
print(f"{12345:<5} Kitas tekstas")  # 12345 Kitas tekst
print(f"{12345:<1} Kitas tekstas")  # 12345 Kitas tekst

# skaičių formatavimas su ju stumimu į centrą
print(f"{12345:^10} Kitas tekstas")  #   12345    Kitas tekstas
print(f"{12345:^5} Kitas tekstas")  # 12345 Kitas tekst
print(f"{12345:^1} Kitas tekstas")  # 12345 Kitas tekst

# Į tekstą galime įterpti specialius simbolius, tokius kaip \n, \t, \", \', \\.

# \n - nauja eilutė
text = "Hello,\nWorld!"
print(text) # Hello,
            # World!

# \t - tabuliacija
text = "Hello,\tWorld!"
print(text) # Hello,  World!

# \" - kabutės
text = "Hello, \"World!\""
print(text) # Hello, "World!"

# \' - apostrofas
text = "Hello, \'World!\'"
print(text) # Hello, 'World!'

# \\ - atvirkštinis brūkšnys
text = "Hello, \\World!"
print(text) # Hello, \World!

# Specialieji simboliai gali būti naudojami ir f string
a = 10
b = 20
text = f"Suma:\t{a + b}\nSkirtumas:\t{a - b}"
print(text) # Suma:	30
            # Skirtumas:	-10

# Specialieji simboliai gali būti naudojami ir trijų kabučių simbolyje
text = """Hello,
\tWorld!"""
print(text) # Hello,
            # 	World!

# Tekstas tai masyvas iš simbolių
# Mes galime praeiti per tekstą naudodami ciklus

text = "Hello, World!"

# foreach ciklas
for letter in text:
    print(letter)

# for ciklas
for i in range(len(text)):
    print(text[i])

# for su enumerate
for i, letter in enumerate(text):
    print(i, letter)

# taip pat galime paimti sub tekstą arba simbolį

# sub tekstas
print(text[7:12]) # World
print(text[7:]) # World!
print(text[:5]) # Hello
print(text[:]) # Hello, World!
print(text[::2]) # Hlo ol!
print(text[::-1]) # !dlroW ,olleH
print(text[-1]) # !
print(text[-2]) # d
print(text[5]) # ,

# bet mes negalime pakeisti simbolio ar sub teksto
# nes tekstas yra nekeičiamas
# text[0] = "h" # TypeError: 'str' object does not support item

# galima tekstą paversti į masyvą
arr = list(text)
print(arr) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# Daubui su tekstais yra naudingos įvairios funkcijos

# Visų raidžių pavertimas į mažąsias
text = "Hello, World!"
print(text.lower()) # hello, world!

# Visų raidžių pavertimas į didžiąsias
text = "Hello, World!"
print(text.upper()) # HELLO, WORLD!

# Teksto pakeitimas
text = "Hello, World!"
print(text.replace("Hello", "Goodbye")) # Goodbye, World!

# Teksto padalijimas
text = "Hello, World!"
print(text.split()) # ['Hello,', 'World!']
print(text.split(",")) # ['Hello', ' World!']

# Teksto išvalymas nuo tarpų pradžioje ir pabaigoje
text = "                       Hello, World! "
print(text.strip()) # Hello, World!

# Teksto išvalymas nuo tarpų pradžioje
text = "                       Hello, World! "
print(text.lstrip()) # Hello, World!

# Teksto išvalymas nuo tarpų pabaigoje
text = "                       Hello, World! "
print(text.rstrip()) #                        Hello, World!

# Teksto tikrinimas ar prasideda arba baigiasi tam tikru tekstu
text = "Hello, World!"
print(text.startswith("Hello")) # True

text = "Hello, World!"
print(text.endswith("World!")) # True

# Teksto ilgis
text = "Hello, World!"
print(len(text)) # 13

# Teksto simbolių kiekis
text = "Hello, World!"
print(text.count("l")) # 3

# Teksto simbolio indeksas iš kairės
text = "Hello, World!"
print(text.index("l")) # 2

# Teksto simbolio indeksas iš dešinės
text = "Hello, World!"
print(text.rindex("l")) # 10

# Patikrinimas ar tekstas yra skaitinis
text = "123"
print(text.isdigit()) # True

text = "123.45"
print(text.isdigit()) # False

# Patikrinimas ar tekstas yra skaitinis su kableliu
text = "123"
print(text.isdecimal()) # True

text = "123.45"
print(text.isdecimal()) # False

# Patikrinimas ar tekstas yra skaitinis su kableliu ir ženklu
text = "123"
print(text.isnumeric()) # True

text = "123.45"
print(text.isnumeric()) # False

# Patikrinimas ar tekstas yra sudarytas tik iš raidžių
text = "Hello"
print(text.isalpha()) # True

text = "Hello, World!"
print(text.isalpha()) # False

# Patikrinimas ar tekstas yra sudarytas tik iš raidžių ir skaičių
text = "Hello123"
print(text.isalnum()) # True

text = "Hello, World!"
print(text.isalnum()) # False

# Patikrinimas ar tekstas yra sudarytas tik iš mažųjų raidžių
text = "hello"
print(text.islower()) # True

text = "Hello"
print(text.islower()) # False

# Patikrinimas ar tekstas yra sudarytas tik iš didžiųjų raidžių
text = "HELLO"
print(text.isupper()) # True

text = "Hello"
print(text.isupper()) # False

# Patikrinimas ar tekstas prasideda didžiąja raide
text = "Hello"
print(text.istitle()) # True

text = "hello"
print(text.istitle()) # False

# Pirmos raidės padarymas didžiąja
text = "hello"
print(text.capitalize()) # Hello

# Kiekvienos žodžio pirmos raidės padarymas didžiąja
text = "hello, world!"
print(text.title()) # Hello, World!

# Teksto sujungimas
text = "Hello, World!"
print(" ".join(text)) # H e l l o ,   W o r l d !

# Teksto sujungimas su kableliu
text = "Hello, World!"
print(",".join(text)) # H,e,l,l,o,,, ,W,o,r,l,d,!

# Teksto sujungimas su kableliu ir tarpais
text = "Hello, World!"
print(", ".join(text)) # H, e, l, l, o, ,,  , W, o, r, l, d, !

# Masyvo elementų pavertimas į tekstą
arr = [1, 2.5, "Hello", True, [1, 2, 3], (4, 5, 6)]
str_arr = list(map(str, arr))
print(str_arr) # ['1', '2.5', 'Hello', 'True', '[1, 2, 3]', '(4, 5, 6)']

# Masyvo elementų sujungimas į tekstą
print(" ".join(str_arr)) # 1 2.5 Hello True [1, 2, 3] (4, 5, 6)
