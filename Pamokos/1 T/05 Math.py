# Norėdami naudoti math modulio funkcijas, pirmiausia turite jį importuoti.
import math


# Apskaičiuoja kvadratinę šaknį
root = math.sqrt(16)
print(root)  # 4.0

# Apskaičiuoja skaičių pakelta laipsniu
# Tas pats kaip ir 2 ** 3
power = math.pow(2, 3)
print(power)  # 8.0

# Apskaičiuoti kitokį šaknies laipsnį galima taip:
# Tai yra 3 laipsnio šaknis iš 27
cubic_root = math.pow(27, 1/3)
print(cubic_root)  # 3.0

# Taip pat galima naudoti math modulio funkciją
cubic_root = math.cbrt(27)
print(cubic_root)  # 3.0

# Suapvalina skaičių į mažiausią sveikąjį skaičių
floor = math.floor(10.5)
print(floor)  # 10

# Suapvalina skaičių į didžiausią sveikąjį skaičių
ceil = math.ceil(10.5)
print(ceil)  # 11

# Suapvalina skaičių į artimiausią sveikąjį skaičių
# Tai ne math modulio funkcija, dėl to nereikia rašyti math.round()
round_number = round(10.5)

# Modulis keičia skaičių į teigiamą
absolute = math.fabs(-10)
print(absolute)  # 10.0

# Absoliutus skaičius gali būti ir be math modulio
absolute = abs(-10)
print(absolute)  # 10

# Absoliutus skaičius gali būti ir su realiuoju skaičiumi
absolute = abs(-10.5)
print(absolute)  # 10.5

# Visos trigonometrinės funkcijos veikia su radianais
# Todėl reikia konvertuoti laipsnius į radianus
# 90 laipsnių yra pi / 2 radianų
radians = math.radians(90)

# Apskaičiuoja sinusą
sin = math.sin(radians)
print(sin)  # 1.0

# Apskaičiuoja kosinusą
cos = math.cos(radians)
print(cos)  # 6.123233995736766e-17

# Apskaičiuoja tangento
tan = math.tan(radians)
print(tan)  # 1.633123935319537e+16

# Apskaičiuoja arko sinusą
# Rezultatas yra radianais
asin = math.asin(1)
print(asin)  # 1.5707963267948966

# Apskaičiuoja arko kosinusą
# Rezultatas yra radianais
acos = math.acos(0)
print(acos)  # 1.5707963267948966

# Apskaičiuoja arko tangento
# Rezultatas yra radianais
atan = math.atan(1)
print(atan)  # 0.7853981633974483

# Konvertuoja radianus į laipsnius
degrees = math.degrees(atan)
print(degrees)  # 45.0