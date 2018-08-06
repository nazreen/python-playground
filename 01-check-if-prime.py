from math import sqrt; from itertools import count, islice

# input can either be a single number or a comma separated list of numbers

def check():
    user_input = input('What is the number?\n')
    inputType = 'int'

    if ',' in user_input:
        inputType = 'list'

    def isPrime(n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

    if inputType is 'list':
        inputArray = user_input.split(',')
        arePrime = []
        areNotPrime = []
        for number in inputArray:
            itemIsPrime = isPrime(int(number))
            if itemIsPrime:
                arePrime.append(number)
            else:
                areNotPrime.append(number)
        print(f'Prime numbers: {str(arePrime)}')
        print(f'NOT Prime numbers: {str(areNotPrime)}')
    else:
        print(isPrime(int(user_input)))
    check()

check()