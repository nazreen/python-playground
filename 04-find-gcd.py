from fractions import gcd

def check():
    user_input = input('What is the number?\n')
    numbers = user_input.split(',')

    first = int(numbers[0])
    second = int(numbers[1])

    print(gcd(first,second))

check()