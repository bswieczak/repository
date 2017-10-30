class Przedmiot:
    id = None
    typ = None
    nazwa = None

    def __init__(self, id, typ, nazwa):
        self.id = id
        self.typ = typ
        self.nazwa = nazwa

    def toString(self):
        return "[{}, {}, {}]".format(self.id, self.typ, self.nazwa)

class KolekcjaDomowa:

    __kolekcja = []

    def dodajPrzedmiot(self, przedmiot):
        self.__kolekcja.append(przedmiot)

    def filtruj(self, filter):
        list = []
        for przedmiot in self.__kolekcja:
            if(filter(przedmiot) == True):
                list.append(przedmiot)
        return list

    def wyswietlCalaKolekcje(self):
        for i in self.__kolekcja:
            print (i.toString())

    def wyswietlOTypie(self, typ):
        for i in self.__kolekcja:
            if(i.typ == typ):
                print(i)

    def usunPzedmiot(self, id):
        for i in self.__kolekcja:
            if(i.id == id):
                self.__kolekcja.remove(i)
                return True
        return False

    def modyfikuj(self, id, przedmiot):
        for i in self.__kolekcja:
            if(i.id == id):
                i.typ = przedmiot.typ
                i.nazwa = przedmiot.nazwa


ob = KolekcjaDomowa()

ob.dodajPrzedmiot(Przedmiot(1,"ksiazka","clean code"))
ob.dodajPrzedmiot(Przedmiot(2,"ksiazka","clean code 2"))
ob.dodajPrzedmiot(Przedmiot(3,"obraz","van gog"))
ob.dodajPrzedmiot(Przedmiot(3,"obraz","van gog2"))


ob.wyswietlCalaKolekcje()

print (ob.usunPzedmiot(1))
