'''
FINDING PI TO THE Nth DIGIT

Name = pi.py
Author = Tola Shobande (tolajs)
Algorithm = Chudnovsky algorithm
'''
from decimal import Decimal
from decimal import getcontext
from math import factorial 

def get_sum(value):
    '''
get_sum(value) ->
    Returns the sum of the Chudnovsky series.
    value: The amount of iterations to sum up in the series.
    '''
    
    # Decimal precision to 12000 digits
    getcontext().prec = 12000
    sum = 0
    
    for i in range(value):
        numerator = factorial(6*i) * (545140134*i + 13591409)
        denominator = factorial(3*i) * factorial(i)**3 * (-262537412640768000)**i
        
        sum += Decimal(numerator)/Decimal(denominator)
    return sum

def get_pi(value):
    '''
get_pi(value) ->
    Returns the approximate value of the pi by dividing the 
    constant with the sum of the series.
    value: The amount of iterations to sum up in the series.
    '''
    
    sum = get_sum(value)
    pi = (Decimal(426880) * Decimal(10005).sqrt()) / sum
    return pi

def check_input(entry):
    if not entry.isdigit():
        print('Input is not a non-negative whole number')
        return False
    elif int(entry) > 10000:
        print('Enter a number in range (1-10000)')
        return False
    return True
    
def main():
    while True:
        entry = input('Enter the amount of Pi digits you want to see from (1-10000) or "quit" to exit: ')
        if entry == 'quit':
            break
        if check_input(entry):
            s = int(entry)
            num = 710
            
            if s <= 2000:
                num = 150
            elif s <= 5000:
                num = 400
            elif s <= 7000:
                num = 600 
               
            if s == 1:
                print(str(get_pi(num))[0])
            else:
                print((str(get_pi(num))[:s+1]))
            break          


if __name__ == '__main__':
    main()