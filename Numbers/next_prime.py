'''
FIND THE NEXT PRIME NUMBER UNTILL THE USER DECIDES TO STOP

Name = next_prime.py
Author = Tola Shobande (tolajs)
Comment: Just practing how to use generators.
Reference = 'https://github.com/Silverneo/pylearn/blob/master/prime.py'
'''

def isprime(value):
    '''
isprime(value) ->
    Returns True if the given parameter value is a prime number.
    '''
    for i in range(3, int(value**0.5)+1, 2):
        if value % i == 0:
            return False
    return True

def gen_prime():
    '''
gen_prime() ->
    Generator function that yields a value given isprime() retuns True  
    '''
    value = 3
    yield 2
    
    while(True):
        if isprime(value):
            yield value
        value += 2
        
def main():
    print("Press Enter to generate the next prime number or Q to quit.")
    g = gen_prime()
    
    while(True):
        entry = input('-> ')
        
        if entry.lower() == 'q':
            break
        else:
            print(next(g))
            
if __name__ == '__main__':
    main()