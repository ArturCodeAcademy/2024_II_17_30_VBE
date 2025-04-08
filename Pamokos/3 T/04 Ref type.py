# Kopijojant klases objektus, mes kopijuojame tik nuorodas į objektus,
# todėl jei keičiame objekto kintamąjį, tai keičiasi ir kopijuotas objektas.

class Computer:
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd


pc1 = Computer("Intel i5", 8, 500)
pc2 = pc1

print(pc1.cpu)  # Intel i5
print(pc2.cpu)  # Intel i5

pc1.cpu = "Intel i7"

print(pc1.cpu)  # Intel i7
print(pc2.cpu)  # Intel i7

# Kaip matome, keičiant pc1.cpu, keičiasi ir pc2.cpu.
# Jei norime sukurti objekto kopiją, turime naudoti copy() metodą.


class Monitor:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    # Metodas, kuris kopijuoja objektą.
    def copy(self):
        return Monitor(self.brand, self.size)


monitor1 = Monitor("Samsung", 24)
monitor2 = monitor1.copy()

print(monitor1.brand)  # Samsung
print(monitor2.brand)  # Samsung

monitor1.brand = "LG"

print(monitor1.brand)  # LG
print(monitor2.brand)  # Samsung

# Dabar, keičiant monitor1.brand, monitor2.brand nesikeičia.
# Nes monitor2 yra kopija monitor1, o ne nuoroda į monitor1.
