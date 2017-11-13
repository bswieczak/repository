
def printer(path, width):
    with open(path) as files:
        list = []
        for line in files.readlines():
            line = line.strip()
            if(len(line)< int(width)):
                print(line.center(width))
            else:
                print (line[0 : width])

width = input('Podaj dlugosc: ' )

printer('text.txt', int(width))