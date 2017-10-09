N = input('Ilosc do pobrania: \n');
from_nr = input('W zakresie od: \n')
to_nr = input('do: \n')
is_reverse = input('Posortowane malejaco ? [y/n]')

li =[]

for i in range(int(N)):
    licz = input("Podaj liczbe: ")
    li.append(int(licz))

if(is_reverse is 'y'):
    li.sort(reverse=True)
else:
    li.sort()

li2 = []
for i in range(len(li)):
    if(li[i]>int(from_nr) and li[i]<int(to_nr)):
        li2.append(li[i])

print(li2)

