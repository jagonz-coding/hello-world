#Name: Juan Gonzalez
#ID: 1808943

curr_pass = input()
new_pass = ''

i = 0
while i < len(curr_pass):
    char = curr_pass[i]
    if char == 'i':
        new_pass = new_pass + '!'
    elif char == 'a':
        new_pass = new_pass + '@'
    elif char == 'm':
        new_pass = new_pass + 'M'
    elif char == 'B':
        new_pass = new_pass + '8'
    elif char == 'o':
        new_pass = new_pass + '.'
    else:
        new_pass = new_pass + char
    i += 1

new_pass = new_pass + "q*s"

print(new_pass)