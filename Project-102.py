print('Are You Bored By Calculating Interests for loan you took from bank?')
print("Don't worry because I got you covered")

q = False
while q == False:
    p = int(input('Enter The Money You Borowed: '))
    r = int(input('Enter The Rate Of Interst at which you got loan(% per annum): '))
    t = int(input('For How Long you are planning to take the loan?(Years): '))
    a = (p*r*t)/100
    print('Extra Amount you will have to pay:', a)
    print('Total amount you will have to pay after ', t ,'Years: ', p+a)

    quit = input('Do you want to quit or calculate again?(q/c)')

    if(quit == 'q'):
        q = True
    else:
        p = 0
        r = 0
        t = 0
        a = 0