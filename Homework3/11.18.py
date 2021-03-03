#Name: Juan Gonzalez
#ID: 1808943

list = input().split()
newlist = []

for x in list:
    x = int(x)
    if x >= 0:
        newlist.append(x)

newlist.sort()
for num in newlist:
    print(num, end=' ')