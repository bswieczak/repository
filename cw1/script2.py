li = []

for i in range(0,3):
    number = input('Podaj liczbe: \n')
    li.append(number)

li.sort(reverse=True)

print(li[0])