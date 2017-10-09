small = []
huge = []
for i in range(65,123):
    if(i<=90):
        huge.append(chr(i))
    elif(i>=97):
        small.append(chr(i))

for i in range(len(small)):
    print('{}, {}'.format(huge[i],small[i]))