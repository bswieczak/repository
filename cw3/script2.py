import math

class Punkt2D:
    x = None
    y = None

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def odleglosc(self, p):
        return math.sqrt(pow(self.x - p[0], 2) + pow(self.y - p[1], 2))

class Punkt3D(Punkt2D):
    z = None

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def odleglosc(self, p):
        return math.sqrt(pow(self.x - p[0], 2) + pow(self.y - p[1], 2)+ pow(self.z - p[2], 2))


punkt2d = Punkt2D(1,2)

print (punkt2d.odleglosc((2,1)))

punkt3d = Punkt3D(1,2,3)

print (punkt2d.odleglosc((3,2,1)))
