#Name: Juan Gonzalez
#ID: 1808943

import math

print("Enter wall height (feet):")
height = int(input())
print("Enter wall width (feet):")
width = int(input())

pa_area = width * height
amt_paint = pa_area / 350

num_cans = math.ceil(amt_paint)

print('Wall area: ', end='')
print(pa_area, 'square feet')
print('Paint needed: ', end = '')
print('{:.2f}'.format(amt_paint), 'gallons')
print('Cans needed:', num_cans, 'can(s)\n')

pa_col = {'red': 35, 'blue': 25, 'green': 23}
print('Choose a color to paint the wall:')
co_choice = input()
print("Cost of purchasing", co_choice, "paint: $", end = '')
print(str(num_cans * pa_col[co_choice]))
