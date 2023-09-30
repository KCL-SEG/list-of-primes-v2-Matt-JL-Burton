"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    i = 2
    while (len(list) < number_of_primes):
        prime = True
        for j in range(len(list)):
            if i%list[j] == 0:
                prime=False
        if prime:
            list.append(i)
        i = i + 1         
    return list


primes(20)