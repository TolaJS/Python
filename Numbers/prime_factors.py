'''
FIND THE PRIME FACTORS A NUMBER THE USER ENTERS

Name = prime_factors.py
Author = Tola Shobande (tolajs)
'''
#From the 'next_prime.py' script
from next_prime import isprime

def prime_factors(value):
    '''
prime_factors(value) -> 
    Returs a set of all the prime factors of the parameter value
    '''
    pass

def check_entry(value):
    '''
check_entry(vale) ->
    Returns True is the parameter is an integer greater than 1
    '''
    if value.isdigit() and int(value) >1:
        return True
    else:
        print('Input is not a non-negative whole number greater than 1!')
        return False

def main():
    print("Enter any non-negative whole number greater than 1 to reveal its prime factors:")
    while True:
        s = set()
        entry = input("-> ")
    
        if check_entry(entry):
            entry = int(entry)
        else: continue
        
        if isprime(entry):
            s.add(entry),s.add(1)
            print(f"Prime factors of {entry} are {s}")
            break
        
        print(f"Prime factors of {entry} are{prime_factors(entry)}")
                  
if __name__ == '__main__':
    main()