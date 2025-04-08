# Mes taip pat galime kurti objektų masyvus.

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Sukuriamas objektų masyvas.
points = \
    [
        Point2D(0, 0),
        Point2D(1, 1),
        Point2D(2, 2),
        Point2D(3, 3),
        Point2D(4, 4)
    ]

# Objektų masyvo elementai pasiekiami naudojant indeksą.
print(points[0].x, points[0].y)  # 0 0

# Mes taip pat galime pridėti naują objektą į masyvą.
points.append(Point2D(5, 5))

# Galime paskaičiuoti taškų centroidą.
# Centroidas yra taškas, kuris yra vidurio taškas.

centroid = Point2D(0, 0)  # Sukuriame centroidą su pradinėmis koordinatėmis.

# Pridedame visų taškų x ir y koordinates.
for point in points:
    centroid.x += point.x
    centroid.y += point.y

# Skaičiuojame centroido x ir y koordinates.
# Daliname iš taškų skaičiaus.
centroid.x /= len(points)
centroid.y /= len(points)

print("Taškai:")
for point in points:
    print(f"({point.x}; {point.y})")
print(f"Centroidas: ({centroid.x}; {centroid.y})")  # Centroidas: 2.5 2.5