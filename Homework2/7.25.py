#Name: Juan Gonzalez
#ID: 1808943



def exact_change(user_total):
    numpennies = int(user_total)
    numdollars = 0
    numquarters = 0
    numdimes = 0
    numnickels = 0
    if numpennies == 0:
        print('no change')
    while numpennies >= 5:
        if numpennies >= 100:
            numdollars += 1
            numpennies -= 100
        elif numpennies >= 25:
            numquarters += 1
            numpennies -= 25
        elif numpennies >= 10:
            numdimes += 1
            numpennies -= 10
        elif numpennies >= 5:
            numnickels += 1
            numpennies -= 5
    if numdollars > 0:
        if numdollars > 1:
            print(numdollars, 'dollars')
        elif numdollars == 1:
            print('1 dollar')

    if numquarters > 0:
        if numquarters > 1:
            print(numquarters, 'quarters')
        elif numquarters == 1:
            print('1 quarter')

    if numdimes > 0:
        if numdimes > 1:
            print(numdimes, 'dimes')
        elif numdimes == 1:
            print('1 dime')

    if numnickels > 0:
        if numnickels > 1:
            print(numnickels, 'nickels')
        elif numnickels == 1:
            print('1 nickel')

    if numpennies > 0:
        if numpennies > 1:
            print(numpennies, 'pennies')
        elif numpennies == 1:
            print('1 penny')

exact_change(input())
