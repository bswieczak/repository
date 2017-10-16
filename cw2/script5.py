import os


def generator(path):
    for x in os.listdir(path):
        x.split('.')
        if x[1] == 'txt':
            yield x

a = generator('C:\\Users\\student\\Documents\\a')
