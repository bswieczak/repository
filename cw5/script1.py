
def printer(path, width):
    with open(path) as files:
        for line in files.readlines():
            if(len(line)< int(width)):
                print(line)
            else:
                print (line[0 : width])

width = input('Podaj dlugosc: ' )

printer('text.txt', int(width))