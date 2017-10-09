small = []
huge = []
for i in range(65,123):
    if(i<=90):
        small.append(chr(i))
    elif(i>=97):
        huge.append(chr(i))

print(small)
print(huge)