#Name: Juan Gonzalez
#ID: 1808943

def exact_change(user_total):
    dol = 0
    qua = 0
    dime = 0
    nick = 0
    pen = 0
    while user_total > 0:
        if user_total > 100:
            dol += 1
            user_total -= 100
        elif user_total > 25:
            qua += 1
            user_total -= 25
        elif user_total > 10:
            dime += 1
            user_total -= 10
        elif user_total > 5:
            nick += 1
            user_total -= 5
        elif user_total > 1:
            pen += 1
            user_total -= 1
    if dol > 0:
        if dol > 1:
            print(dol, ' dollars')
        elif dol == 1:
            print('1 dollar')
            
    if qua > 0:
        if qua > 1:
            print(qua, ' quarters')
        elif qua == 1:
            print('1 quarter')

    if dime > 0:
        if dime > 1:
            print(dime, ' dimes')
        elif dime == 1:
            print('1 dime')

    if nick > 0:
        if nick > 1:
            print(nick, ' nickels')
        elif nick == 1:
            print('1 nickel')

    if pen > 0:
        if pen > 1:
            print(pen, ' pennies')
        elif pen == 1:
            print('1 penny')


exact_change(int(input()))