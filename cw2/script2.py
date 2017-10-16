import math

def function(n):
    fi = 1.6180339887
    return [round((math.pow(fi,x) - pow((1-fi),x))/(math.sqrt(5))) for x in range(n)]

print (function(10))