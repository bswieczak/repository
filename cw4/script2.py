import sys

def converter(f):
    dict = {}
    with open(f) as f:
        for str in f.readlines():
            if(len(str)>=2):
                str = str.split(':')
                dict[str[0]] = str[1].rstrip()
    return dict

print(converter(sys.argv[1]))