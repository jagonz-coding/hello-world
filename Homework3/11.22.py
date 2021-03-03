#Name: Juan Gonzalez
#ID: 1808943

string = input()
newstring = string.split(" ")
for name in newstring:
    print(name, newstring.count(name))