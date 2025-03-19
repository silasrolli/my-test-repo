import math

class Vector3:
    def __init__(self, x=0, y=0, z=0):

        self.x = x
        self.y = y
        self.z = z

    def len(self):

        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

v1 = Vector3(3, 4, 12)
print(f"Vektor: ({v1.x}, {v1.y}, {v1.z})")
print(f"Länge des Vektors: {v1.len():.2f}")

v2 = Vector3()
print(f"Null-Vektor: ({v2.x}, {v2.y}, {v2.z})")
print(f"Länge des Null-Vektors: {v2.len():.2f}")

