# while ciklas vykdomas tol, kol sąlyga yra True
# Jis yra panašus į if sąlygą, tik jis vykdomas tol, kol sąlyga yra True

# Kodas vykdomas tol, kol a yra mažesnis už 10
a = 0
while a < 10:
    print(a)
    a += 1

# Sąlyga galima būti bet kokia, pavyzdžiui:
# Kodas vykdomas tol, kol a yra mažesnis už 10 ir b yra mažesnis už 5
a = 0
b = 0

while a < 10 and b < 5:
    print(a, b)
    a += 1
    b += 1

# Stengiamės nesukurti begalinio ciklo, nes jis gali užšalti programą
# Pvz.:
# while True: # True visada yra True, todėl šis ciklas bus begalinis
#     print("Begalinis ciklas")

