#Name: Juan Gonzalez
#ID: 1808943

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())

works = False
x = 0
y = 0

for i in range(-10,11):
    for j in range(-10, 11):
        if ((((num1 * i) + (num2 * j)) == num3) and (((num4 * i) + (num5 * j)) == num6)):
            x = i
            y = j
            works = True
            break
    if works == True:
        break

if works == True:
    print(x, y)
else:
    print("No solution")