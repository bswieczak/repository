import sys, itertools

def counter(path):
    with open(path) as file:
        string = file.read().split()
        count = 1
        while len(string)!=0:
            for i in range(len(string)):


counter(sys.argv[1])