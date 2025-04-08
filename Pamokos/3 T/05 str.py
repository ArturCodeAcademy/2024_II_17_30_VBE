class TikTakToeGameResult:
    def __init__(self, rock, paper, scissors):
        self.rock = rock
        self.paper = paper
        self.scissors = scissors


results = TikTakToeGameResult(5, 8, 10)

# Jei norime objektą sukonvertuoti į string'ą, turime apibrėžti __str__ metodą.
# Be šio metodo, mes gauname objekto atminties adresą ir klasės pavadinimą.

obj_as_str = str(results)
print(obj_as_str)  # <__main__.TikTakToeGameResult object at 0x0000022E8D3C5A60>


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    # __str__ metodas turi grąžinti string'ą.
    def __str__(self):
        return f"{self.name} - {self.breed} - {self.age}"


dog = Dog("Rex", "Labrador", 5)
sog_as_str = str(dog)
# Dabar mes gauname rezultatą kuris mum buvo reikalingas.
print(sog_as_str)  # Rex - Labrador - 5
print(dog) # Rex - Labrador - 5
