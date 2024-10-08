# Norint išvesti tekstą į ekraną galima naudoti print() funkciją.
print("Hello World!")  # Hello World!

# Jeigu norime praleisti eilutę, galime į print() nieko nerašyti.
print()  # Išveda tuščią eilutę.

# Taip pat galime išvesti kintamąjį.
a = 5
print(a)  # 5

# Kintamąjį galime išvesti ir su tekstu.
print("a =", a)  # a = 5

# Kintamieji gali būti ir kitų tipų.
b = 3.14
print("b =", b)  # b = 3.14

# Kintamieji gali būti ir tekstai.
c = "Labas"
print("c =", c)  # c = Labas

# Argumentų perduoti galima ir daugiau, juos atskirdami kableliais.
# Jie bus išvesti atskiriant tarpu.
print(a, b, c)  # 5 3.14 Labas

# Argumentai gali būti ir skaičiai.
print(1, 2, 3)  # 1 2 3

# Jei norime išvesti tekstą be naujos eilutės,
# galime nurodyti, kad nereikia eilutės pabaigos.
print("Hello ", end="") # Hello
print("World!")  # Hello World!

# Jei norime maisyti tekstą su kintamaisiais, prieš kabutę rašome f.
# O kintamąjį įdedame į {} skliaustus.
a = 5
print(f"a = {a}")  # a = 5

# Jei norime, kad skaičius būtų išvestas su tam tikru tikslumu,
# galime nurodyti formatą.
pi = 3.14159265359
print(f"pi = {pi:.0f}")  # pi = 3
print(f"pi = {pi:.1f}")  # pi = 3.1
print(f"pi = {pi:.2f}")  # pi = 3.14
print(f"pi = {pi:.3f}")  # pi = 3.142
print(f"pi = {pi:.4f}")  # pi = 3.1416
print(f"pi = {pi:.5f}")  # pi = 3.14159
print(f"pi = {pi:.15f}")  # pi = 3.141592653590000

# Jei reikia nuskaityti duomenis nuo vartotojo, naudojama input() funkcija.
# Funkcija input() grąžina įvestą tekstą, kurį galima panaudoti kaip norim.
text_from_user = input()  # Programa sustos ir lauks kol vartotojas įves tekstą ir paspaus enter.
print(text_from_user)  # Atspausdins įvestą tekstą.

# Taip pat į input() funkciją galima paduoti tekstą, kuris bus atvaizduotas vartotojui.
text_from_user = input("Įveskite tekstą: ")  # Programa sustos ir lauks kol vartotojas įves tekstą ir paspaus enter.
print(text_from_user)  # Atspausdins įvestą tekstą.

name = input("Įveskite savo vardą: ")  # Programa sustos ir lauks kol vartotojas įves tekstą ir paspaus enter.
print(f"Sveiki, {name}!")  # Atspausdins įvestą vardą.

# Specialiaji simboliai:
# \n - nauja eilutė
# \t - tabuliacija
# \\ - atspausdina \
# \" - atspausdina "
# \' - atspausdina '
print("Hello\nWorld!")  # Hello
                        # World!

print("Hello\tWorld!")  # Hello   World!

print("\\")  # \

print("\"")  # "
print('"')  # "

print("'")  # '
print('\'')  # '

print("\"Hello\" World!")  # "Hello" World!
