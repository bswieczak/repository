def rozkladNaCzynnikiPierwsze(n):
    lista = {}
    while n != 1:
        x = 2
        while n % x != 0:
            x += 1
        if lista.get(x) == None:
            lista[x] = 1
        else:
            lista[x] = lista[x] + 1
        n = n / x
    return lista.items()

print rozkladNaCzynnikiPierwsze(756)
