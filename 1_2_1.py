import math
import sys

def is_prime(n):
    result = True
    for i in range(2, int(math.sqrt(n)) + 1):
      if not (n / i - n // i):
          result = False
          break
    return result


def test_prime():
    result = True
    data = [(2, 1), (3, 1), (5, 1), (11, 1) , (12, 0), (16, 0), (25, 0),
            (29, 1), (31, 1), (149, 1), (150, 0), (151, 1), (240, 0)
            ]
    for i in data:
        if is_prime(i[0]) != bool(i[1]):
            print('   ', is_prime(i[0]), '!=', bool(i[1]))
            result = False
            break
    return result


def next_prime(number):
    number += 1
    while True:
        if is_prime(number):
            return number
        number += 1


def test_next_prime():
    result = True
    data = [(2, 3), (7, 11), (31, 37), (139, 149)]
    for i in data:
        if next_prime(i[0]) != i[1]:
            print('   ', next_prime(i[0]), '!=', i[1])
            result = False
            break
    return result


def get_factors(number):
    factors = []
    factor = 2
    while number != 1:
        if not (number / factor - number // factor):
            factors.append(factor)
            number = number // factor
        else:
            factor = next_prime(factor)
    return factors


def test_get_factors():
    result = True
    data = [(75, [3, 5, 5]), (35, [5, 7]), (150, [2, 3, 5, 5])]
    for i in data:
        if get_factors(i[0]) != i[1]:
            print('   ', get_factors(i[0]), '!=', i[1])
            result = False
            break
    return result


def main(number):
    factors = ' '.join([str(i) for i in get_factors(int(number))])
    print(factors)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print("Test prime - ", test_prime() and 'Ok')
        print("Test next prime - ", test_next_prime() and 'Ok')
        print("Test get factors - ", test_get_factors() and 'Ok')
    else:
        number = input()
        main(number)