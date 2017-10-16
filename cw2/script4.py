import math

def function(list, pkt):
    dist = lambda x,y : math.sqrt(pow(pkt[0] - x, 2) + pow(pkt[1] - y, 2))
    return [(dist(p[0],p[1]), p) for p in list]

list = [(1,1), (0,1),(3,2), (5,2)]
pkt = (0,0)

print (function(list, pkt))