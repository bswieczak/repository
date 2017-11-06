import sys

def function():
    if(sys.argv[1] == '-'):
        stoper = True
        while stoper:
            string = input('pisz: ')
            if len(string.split("\n"))>0:
                stoper = False
    else:
        with open(sys.argv[1]) as file:
            for line in file.readlines():
                if sys.argv[2] in line:
                    print (line)


function()