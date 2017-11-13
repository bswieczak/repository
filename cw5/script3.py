import re

def validator():
    regex = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    with open('ipV4.txt') as file:
        for ip in file.readlines():
            if(regex.search(ip.strip()) is not None):
                print (ip)


validator()