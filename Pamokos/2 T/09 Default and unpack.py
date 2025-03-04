# Mes galime nurodyti numatytąsias reikšmes parametrams.

def greet(name="John"):
    return f"Hello, {name}!"


# Jei nenurodome parametro, bus naudojama numatyta reiksme
result = greet()
print(result)  # Hello, John!

# Jei nurodome parametra, bus naudojama nurodyta reiksme
result = greet("Alice")
print(result)  # Hello, Alice!


# Numatytosios reikšmės gali būti bet kokio tipo
def sum_two_numbers(a=5, b=10):
    return a + b


# Jei nenurodome parametrų, bus naudojamos numatytos reikšmės
result = sum_two_numbers()
print(result)  # 15

# Jei nurodome vieną parametrą, antram bus naudojama numatyta reikšmė
result = sum_two_numbers(10)
print(result)  # 20

# Jei nurodome abu parametrus, bus naudojamos nurodytos reikšmės
result = sum_two_numbers(10, 20)
print(result)  # 30

# Mes galime pakeisti eiliškumą, nurodydami parametrus
result = sum_two_numbers(b=20, a=10)
print(result)  # 30

# Jei mes turime masyvą, kurį norime išskaidyti į parametrus,
# mes galime tai padaryti su *.
def sum_three_numbers(a, b, c):
    return a + b + c


arr = [5, 10, 15]

result = sum_three_numbers(arr[0], arr[1], arr[2])
print(result)  # 30

a, b, c = arr  # Išskaidome masyvą į kintamuosius
result = sum_three_numbers(a, b, c)
print(result)  # 30

result = sum_three_numbers(*arr)  # Išskaidome masyvą į parametrus
print(result)  # 30


# Jei mes nežinome, kiek parametrų bus, mes galime naudoti * parametrą
# *nums - tai tuple, kuriame yra visi perduoti parametrai
def sum_numbers(*nums):
    s = 0
    for num in nums:
        s += num
    return s


result = sum_numbers(5, 10, 15, 20)
print(result)  # 50

result = sum_numbers(5, 10, 15, 20, 25, 30)
print(result)  # 105