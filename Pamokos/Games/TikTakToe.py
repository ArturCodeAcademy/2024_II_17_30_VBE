# Importuojamas modulis skirtas valdyti kompiuterio operacine sistema
# Naudojamas tam, kad būtų galima išvalyti ekraną
import os

# kintamieji kuriose saugomi žaidimo laukų reikšmės
# " " - laukas tuščias
# "X" - laukas užimtas kryžiuku
# "O" - laukas užimtas nuliuku

# Pirma eilutė
field_0_0 = " "
field_0_1 = " "
field_0_2 = " "

# Antra eilutė
field_1_0 = " "
field_1_1 = " "
field_1_2 = " "

# Trečia eilutė
field_2_0 = " "
field_2_1 = " "
field_2_2 = " "

# Kintaamasis kuris nurodo kuris žaidėjas dabar turi eiti
# True - kryžiukas
# False - nuliukas
player_x_turn = True

# Kinamasis kuris nurodo ar žaidimas tęsiasi
# True - žaidimas tęsiasi
# False - žaidimas baigtas
game_running = True

# Kinamasis kuris nurodo kas laimėjo
winner = ""

# Žaidimo ciklas
while game_running:

    # Išvalomas ekranas
    # Jei naudojate ne Windows operacinę sistemą, pakeiskite 'cls' į 'clear'
    # Gali neveikti jei naudojate IDE
    os.system('cls')
    print("Kryžiukai nuliukai")

    # Atvaizduojamas žaidimo laukas
    print(f" {field_0_0} | {field_0_1} | {field_0_2} ")
    print("---|---|---")
    print(f" {field_1_0} | {field_1_1} | {field_1_2} ")
    print("---|---|---")
    print(f" {field_2_0} | {field_2_1} | {field_2_2} ")

    print("""
 7 | 8 | 9
---|---|---
 4 | 5 | 6
---|---|---
 1 | 2 | 3
""")

    cell_number = int(input("Įveskite langelio numerį: "))
    cell_free = False  # Kintamasis kuris nurodo ar langelis yra tuščias

    while not cell_free:  # Ciklas tęsiasi tol kol langelis nėra tuščias
        # Tikriname ar langelis yra tuščias
        # Ir priskiriame naują reikšmę langeliui
        # Jei langelis užimtas, prašome įvesti naują langelio numerį
        if cell_number == 1 and field_2_0 == " ":
            cell_free = True
            if player_x_turn:
                field_2_0 = "X"
            else:
                field_2_0 = "O"
        elif cell_number == 2 and field_2_1 == " ":
            cell_free = True
            if player_x_turn:
                field_2_1 = "X"
            else:
                field_2_1 = "O"
        elif cell_number == 3 and field_2_2 == " ":
            cell_free = True
            if player_x_turn:
                field_2_2 = "X"
            else:
                field_2_2 = "O"
        elif cell_number == 4 and field_1_0 == " ":
            cell_free = True
            if player_x_turn:
                field_1_0 = "X"
            else:
                field_1_0 = "O"
        elif cell_number == 5 and field_1_1 == " ":
            cell_free = True
            if player_x_turn:
                field_1_1 = "X"
            else:
                field_1_1 = "O"
        elif cell_number == 6 and field_1_2 == " ":
            cell_free = True
            if player_x_turn:
                field_1_2 = "X"
            else:
                field_1_2 = "O"
        elif cell_number == 7 and field_0_0 == " ":
            cell_free = True
            if player_x_turn:
                field_0_0 = "X"
            else:
                field_0_0 = "O"
        elif cell_number == 8 and field_0_1 == " ":
            cell_free = True
            if player_x_turn:
                field_0_1 = "X"
            else:
                field_0_1 = "O"
        elif cell_number == 9 and field_0_2 == " ":
            cell_free = True
            if player_x_turn:
                field_0_2 = "X"
            else:
                field_0_2 = "O"
        else:
            cell_number = int(input("Langelis užimtas arba neteisingas langelio numeris, įveskite naują langelio numerį: "))

    # Tikriname ar žaidimas baigėsi
    # Tikriname ar yra laimėtojas
    # Tikriname ar yra lygiosios

    if field_0_0 == field_0_1 == field_0_2 != " ":
        game_running = False
        winner = field_0_0
    elif field_1_0 == field_1_1 == field_1_2 != " ":
        winner = field_1_0
        game_running = False
    elif field_2_0 == field_2_1 == field_2_2 != " ":
        winner = field_2_0
        game_running = False
    elif field_0_0 == field_1_0 == field_2_0 != " ":
        winner = field_0_0
        game_running = False
    elif field_0_1 == field_1_1 == field_2_1 != " ":
        winner = field_0_1
        game_running = False
    elif field_0_2 == field_1_2 == field_2_2 != " ":
        winner = field_0_2
        game_running = False
    elif field_0_0 == field_1_1 == field_2_2 != " ":
        winner = field_0_0
        game_running = False
    elif field_0_2 == field_1_1 == field_2_0 != " ":
        winner = field_0_2
        game_running = False
    elif field_0_0 != " " and field_0_1 != " " and field_0_2 != " " and field_1_0 != " " and field_1_1 != " " and field_1_2 != " " and field_2_0 != " " and field_2_1 != " " and field_2_2 != " ":
        game_running = False

    # Pakeičiame žaidėją
    player_x_turn = not player_x_turn

# Išvalomas ekranas
os.system('cls')

# Atvaizduojamas žaidimo laukas
print(f" {field_0_0} | {field_0_1} | {field_0_2} ")
print("---|---|---")
print(f" {field_1_0} | {field_1_1} | {field_1_2} ")
print("---|---|---")
print(f" {field_2_0} | {field_2_1} | {field_2_2} ")

# Išvedame žaidimo rezultatą
if winner == "":
    print("Lygiosios")
else:
    print("Laimėjo: ", winner)

# Laukiame kol žaidėjas paspaus Enter, kad uždaryti programą
# Jei naudojate ne Windows operacinę sistemą, pakeiskite 'pause' į 'read'
# Gali neveikti jei naudojate IDE
os.system('pause')
