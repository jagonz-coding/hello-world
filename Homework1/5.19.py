#Name: Juan Gonzalez
#ID: 1808943

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

print('Select first service:')
f_ser = input()
print('Select second service:')
s_ser = input()

prices = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

print()
print("Davy's auto shop invoice\n")

if str(f_ser) == '-':
    print('Service 1: No service')
else:
    print('Service 1:', f_ser, end='')
    print(', $', end='')
    print(str(prices[f_ser]))

if str(s_ser) == '-':
    print('Service 2: No service')
else:
    print('Service 2:', s_ser, end='')
    print(', $', end='')
    print(str(prices[s_ser]))

print()
print('Total: $', end='')
print(int(prices[f_ser]) + int(prices[s_ser]))
