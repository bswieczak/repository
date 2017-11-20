from xml.dom import minidom
from urllib2 import urlopen

#napisz prosty czytnik RSS. Program ma miec mozliwosc zpamietania ulobionych kanalow. Wiadomosci powinny byc czytelnie sformatowane
class ParseRSS:

    favorites = []

    def parse(self, url):
        self.favorites.append(url)
        disc = {}
        with open('temp.xml', 'rw') as file:
            file.write(urlopen(url).read())
            dom = minidom.parseString(file)
            var = dom.getElementsByTagName('item')


parser = ParseRSS()

