#Name: Juan Gonzalez
#ID: 1808943

print('Birthday Calculator')

print('Current day')
print('Month: ', end='')
c_mon = int(input())
print('Day: ', end='')
c_day = int(input())
print('Year: ', end='')
c_year = int(input())

print('Birthday')
print('Month: ', end='')
b_mon = int(input())
print('Day: ', end='')
b_day = int(input())
print('Year: ', end='')
b_year = int(input())

if c_mon < b_mon:
    age = (c_year - b_year) - 1
elif c_mon == b_mon:
    if c_day < b_day:
        age = (c_year - b_year) - 1
    elif c_day == b_day:
        age = (c_year - b_year)
    else:
        age = (c_year - b_year)
else:
    age = (c_year - b_year)

if (c_mon == b_mon) and (c_day == b_day):
    print('Happy Birthday! You are', age, 'years old!')
else:
    print('You are', age, 'years old.')
