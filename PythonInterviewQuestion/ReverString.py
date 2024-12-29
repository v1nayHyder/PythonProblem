reverse="Hello"
newString=reverse[::-1]
print(newString)
newString2=reverse[len(reverse)::-1]
print(newString2)
newString3 = ''
for x in range(len(reverse) - 1, -1, -1):
    newString3 += reverse[x]
print(newString3)