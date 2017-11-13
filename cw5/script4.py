
#parser pesel zwraca dzien-miesiać-rok i plec
def validator(pesel):
    year = pesel[0:2]
    month = pesel[2:4]
    day= pesel[4:6]
    sex = pesel[6]


validator('')