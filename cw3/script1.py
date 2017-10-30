import math

class liczbaZesolona:

    b = None

    def __add__(self, a):
        return (self.b[0] + a[0], a[1] + self.b[1])

    def __sub__(self, a):
        return (self.b[0] - a[0], self.b[1] - a[1])

    def __mul__(self, a):
        return (self.b[0] * a[0] - a[1] * self.b[1], a[0] * self.b[1] + a[1] * self.b[0])

    def __truediv__(self, a):
        return ((a[0] * self.b[0] - a[1] * self.b[1]) / (self.b[0] * self.b[0] + self.b[1] * self.b[1]),
                (self.b[0] * a[1] - a[0] * self.b[1]) / (self.b[0] * self.b[0] + self.b[1] * self.b[1]))

    def modol(self):
        return math.sqrt(pow(self.b[0], 2) + pow(self.b[1], 2))


obliczenia = liczbaZesolona()

obliczenia.b = (1, 1)

print (obliczenia + (1,1))
print (obliczenia - (1,1))
print (obliczenia * (1,1))
print (obliczenia / (1,1))
print (obliczenia.modol())