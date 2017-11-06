
def converter(string):
    dict = {}
    for str in string.split('\n'):
        if(len(str)>1):
            str = str.split(':')
            dict[str[0]] = str[1]
    return dict

string = '''k1:w2
k2:w2
k3:w3
'''

print(converter(string))