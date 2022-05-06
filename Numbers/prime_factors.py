"""
FIND THE PRIME FACTORS OF A NUMBER THE USER ENTERS

Name = prime_factors.py
Author = Tola Shobande (tolajs)
"""
# From the 'next_prime.py' script
from next_prime import isprime


def factor(value):
    """
    factor(value) ->
        Returns the lowest prime factors of the parameter value
    """
    if value % 2 == 0:
        return 2

    i = 3
    while i * i <= value:
        if value % i == 0:
            return i
        i += 2

    return value


def check_entry(value):
    """
    check_entry(vale) ->
        Returns True if the parameter is an integer greater than 1
    """
    if value.isdigit() and int(value) > 1:
        return True
    else:
        print("Input is not a non-negative whole number greater than 1!")
        return False


def main():
    print("Enter a number to reveal its prime factors:")
    while True:
        facts = []
        entry = input("-> ")

        # Validate entry
        if check_entry(entry):
            entry = int(entry)
        else:
            continue

        # Check if entry is prime
        if isprime(entry):
            print(f"Prime factors are {[entry]}")
            break

        # Find lowest factors of entry
        while entry != 1:
            facts.append(factor(entry))
            entry //= facts[-1]

        print(f"Prime factors are {facts}")
        break


if __name__ == "__main__":
    main()
