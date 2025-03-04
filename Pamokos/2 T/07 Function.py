import math

# Kai mum reikią daryti ką nors daug kartų,
# galime apibrėžti tuos veiksmus funkcijoje
# ir ją iškviesti kiekvieną kartą, kai reikia.

# Tarkime mum reikia išvesti trikampį prieš ir po pagrindinių veiksmų.
# Be funkcijos tai atrodytų taip:

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("Pagrindiniai veiksmai")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print()
# Tai užima daug vietos ir yra neefektyvu.

# Dabar apibrėšime funkciją, kuri išves trikampį:
# Funkcijos apibrėžimas:
# def - funkcijos apibrėžimo raktinis žodis
# trikampis - funkcijos pavadinimas
# () - funkcijos argumentai, bet šiuo atveju jų nėra
def print_rect_triangle():
    print("   /|")
    print("  / |")
    print(" /  |")
    print("/___|")


print_rect_triangle()  # Funkcijos kvietimas
print("Pagrindiniai veiksmai")
print_rect_triangle()  # Funkcijos kvietimas

# Funkcijos kvietimas yra tiesiogiai funkcijos pavadinimas su skliaustais.
# Funkcijos kvietimas yra būtinas, kad funkcija būtų įvykdyta.
# Tokiu būdu galime sumažinti kodą ir padaryti jį tvarkingesnį.
# Funkcijos apibrėžimas turi būti prieš funkcijos kvietimą.

# Taip pat galime naudoti funkcijas tam, kad kodas būtų lengviau suprantamas.

# Funkcijos gali kviesi viena kitą

def print_triangle():
    for i in range(1, 10, 2):
        print(f"{'*' * i:^9}")


def print_hello_between_triangles():
    print_triangle()  # Funkcijos kvietimas iš kitos funkcijos
    print(f"{'Hello':^9}")
    print_triangle()  # Funkcijos kvietimas iš kitos funkcijos


print_hello_between_triangles()  # Funkcijos kvietimas

# Funkcijos gali ne tik atlikti veiksmus, bet ir grąžinti rezultatą.
# Tai padaryti galima naudojant return komandą.

# Tokios funkcijos jau buvo naudojamos anksčiau
# Tai buvo matematinės funkcijos, kurios grąžindavo rezultatą
# Pavyzdžiui:
result = math.sin(0) # Grąžina 0
print(result)  # 0.0

result = math.sqrt(4) # Grąžina 2
print(result)  # 2.0

# Mes patys galime kurti funkcijas, kurios grąžina rezultatą
# Tam reikia naudoti return komandą viduje funkcijos
def read_array_from_file():
    with open("file_with_array.txt", "r") as fin:
        line = fin.readline()
        nums_as_string = line.split()
        array = list(map(int, nums_as_string))
        return array


# Funkcija grąžina masyvą, kuris yra nuskaitytas iš failo
arr = read_array_from_file()
print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Funkcijos gali grąžinti tiek rezultatų, kiek mum reikia
# Tam reikia po return komandos parašyti rezultatus atskirtus kableliu
def get_sum_min_max_from_array():
    array = read_array_from_file()
    return sum(array), min(array), max(array)


# Funkcija grąžina sumą, mažiausią ir didžiausią reikšmę iš masyvo
# Funkcija grąžina tris rezultatus, todėl jie yra atskirti kableliu
sm, mn, mx = get_sum_min_max_from_array()
print(f"Sum: {sm}, Min: {mn}, Max: {mx}")  # Sum: 55, Min: 1, Max: 10

# Taip pat return komanda gali būti naudojama be jokių rezultatų
# Tai yra, jei funkcija grąžina None, tai nereiškia, kad ji nieko negrąžina
# Tai yra naudinga, kai funkcija reikia sustabdyti anksčiau
def print_array():
    array = read_array_from_file()
    if len(array) == 0:
        print("Masyvas tuščias")
        return  # Funkcija sustabdo veikimą čia jei masyvas tuščias

    for i in array:
        print(i, end=" ")
    print()


# Kai mum reikia, kad funkcijos rezultatas butu priklausomas nuo išorinių parametrų
# mes galime nurodyti juos funkcijoje.
# Parametrai nurodomi tarp skliaustu ir atskiriami kableliais.

def sum_two_numbers(a, b):
    return a + b


result = sum_two_numbers(5, 10)
print(result)  # 15

result = sum_two_numbers(10, 20)
print(result)  # 30

num1 = 15
num2 = 25
result = sum_two_numbers(num1, num2)
print(result)  # 40

# Parametrai gali buti bet kokio tipo, pvz. skaiciai, tekstas ir t.t.

def greet(name):
    return f"Hello, {name}!"


result = greet("John")
print(result)  # Hello, John!
