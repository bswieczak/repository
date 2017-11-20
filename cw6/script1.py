import math

def function (number):
    try:
        sqrt = math.sqrt(number)
    except ValueError as ex:
        print('Prawdopodobnie podales liczbe na minusie. Stacktrace: {}'.format(ex))
    else:
        print('Pierwiastek z {} jest rowny {}'.format(number,sqrt))

number = float(input('Podaj liczbę : '))
function(number)