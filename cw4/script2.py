import sys

def converter(file):
    dict = {}
    with open('text.txt') as file:
        for str in file.readlines():
            if(len(str)>=2):
                str = str.split(':')
                dict[str[0]] = str[1].rstrip()
    return dict

print(converter(sys.argv[1]))