import sys

def cezar(file, file2):
    key = 3
    with open(file) as read:
        with open(file2, 'w') as write:
            for string in read.readlines():
                hashed = ''
                for i in range(len(string)):
                    if ord(string[i]) > 122 - key:
                        hashed += chr(ord(string[i]) + key - 26)
                    else:
                        hashed += chr(ord(string[i]) + key)
                write.write(hashed)

cezar(sys.argv[1], sys.argv[2])