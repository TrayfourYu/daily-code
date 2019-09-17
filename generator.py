import math
def is_prime(number):
    if type(number)==int:
        if number > 1:
            if number == 2:
                return True
            elif number % 2 == 0:
                return False
            for current in range(3, int(math.sqrt(number) + 1), 2):
                if number % current == 0:
                    return False
            else:
                return True
        else:
            return False
    else:
        print("必须是整数")

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

def print_successive_primes(iterations, base=7):
    prime_generator = get_primes(0) #实例化
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))



