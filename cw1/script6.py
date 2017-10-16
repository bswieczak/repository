
N = 10

li = []

i = 0;

while(i<N):
    if (i == 0):
        li.append(0)
    elif (i == 1):
        li.append(1)
    elif( i > 1):
        li.append(li[i-1] + li[i-2])
    i=i+1

print(li)

