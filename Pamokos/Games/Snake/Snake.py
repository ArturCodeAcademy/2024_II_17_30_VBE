# Importuojame operacines sistemos moduli ekranui valdyti
import os
# Importuojame random moduli, kad galetume generuoti atsitiktinius skaicius
import random
# Importuojame time moduli, kad galetume valdyti laika
import time
# Importuojame keyboard moduli, kad galetume valdyti klaviatura
import keyboard


class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Sukursime funkcija, kuri nukopijuos koordinates
    def copy(self):
        return Coord(self.x, self.y)

    # Sukursime funkcija, kuri leis mums palyginti koordinates
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Sukursime funkcija, kuri leis mums sudeti koordinates
    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'({self.x}; {self.y})'


# Aprašome nustatymus
map_width = 20  # Zaidimo lango plotis
map_height = 20  # Zaidimo lango aukstis
render_delay = 0.3  # Kiek laiko laukti tarp zaidimo ciklu
score_per_food = 10  # Kiek taškų duoti už vieną maisto gabalėlį

# Aprašome kryptis
UP = Coord(0, -1)  # Aukštyn
DOWN = Coord(0, 1)  # Žemyn
LEFT = Coord(-1, 0)  # Kairėn
RIGHT = Coord(1, 0)  # Dešinėn

# Aprašome simbolius ir spalvas
snake_head_symbol = 'O'  # Gyvatės galvos simbolis
snake_body_symbol = 'o'  # Gyvatės kūno simbolis
food_symbol = '$'  # Maisto simbolis
border_symbol = '#'  # Sienos simbolis
background_symbol = ' '  # Fono simbolis

snake_head_color = '\033[92m'  # Gyvatės galvos spalva (žalia)
snake_body_color = '\033[93m'  # Gyvatės kūno spalva (geltona)
food_color = '\033[36m'  # Maisto spalva (mėlyna)
border_color = '\033[91m'  # Sienos spalva (raudona)
background_color = '\033[0m'  # Fono spalva (balta)

# Aprašome žaidimo kintamuosius
snake = [Coord(map_width // 2, map_height // 2)]  # Gyvatės kūnas
snake += [snake[0] + LEFT, snake[0] + LEFT + LEFT]  # Pradinis gyvatės ilgis
direction = Coord(1, 0)  # Gyvatės judėjimo kryptis
food = Coord()  # Maisto koordinatės
score = 0  # Žaidėjo taškai
render_time = time.time() + render_delay  # Laikas, kada paskutinį kartą atvaizdavome žaidimą


# Sukursime funkcija, kuri atvaizduos zaidimą
def render():
    os.system('cls')  # Išvalome ekraną

    for y in range(map_height):  # Eilutės
        for x in range(map_width):  # Stulpeliai
            if y == 0 or y == map_height - 1 or x == 0 or x == map_width - 1:
                print(border_color + border_symbol, end='')
            elif Coord(x, y) in snake:  # Jei koordinatė yra gyvatės kūne
                if Coord(x, y) == snake[0]:
                    print(snake_head_color + snake_head_symbol, end='')
                else:
                    print(snake_body_color + snake_body_symbol, end='')
            elif Coord(x, y) == food:  # Jei koordinatė yra maisto
                print(food_symbol, end='')
            else:
                print(background_color + background_symbol, end='')
        print()  # Pereiname į naują eilutę
    print()  # Atvaizduojame tuščią eilutę

    # Atvaizduojame informaciją apie žaidimą
    print("\033[0m")  # Nustatome spalvą į numatytąją
    print(f'Taškai: {score}')
    print(f'Gyvatės ilgis: {len(snake)}')


# Sukursime funkcija, kuri nustatys maisto pozicija
def set_food():
    global food

    while True:
        food = Coord(random.randint(1, map_width - 2), random.randint(1, map_height - 2))

        # Patikriname ar maistas nekertasi su gyvate arba nekertasi su siena
        if food not in snake and food.x != 0 and food.x != map_width - 1 and food.y != 0 and food.y != map_height - 1:
            break


# Sukursime funkcija, kuri kerkels gyvate
def move_snake():
    global snake, direction

    new_head = snake[0].copy()  # Nukopijuojame gyvates galva
    new_head += direction  # Pakeiciame gyvates galvos x koordinate
    # Pastumsime gyvates kuno elementus į masivo galą
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
    snake[0] = new_head  # Pakeiciame gyvates galva


# Sukursime funkcija, kuri patikrins ar zaidimas baigesi
def is_game_over():
    head = snake[0]
    # Patikriname ar gyvate kertasi su siena
    if head.x == 0 or head.x == map_width - 1 or head.y == 0 or head.y == map_height - 1:
        return True

    # Patikriname ar gyvate kertasi su savimi
    if head in snake[1:]:
        return True

    return False


set_food()
render()
# Laukiame kol žaidėjas paspaus klavišą
# Duodame žaidėjui laiką pasiruošti
os.system('pause')

while not is_game_over():
    render()
    move_snake()
