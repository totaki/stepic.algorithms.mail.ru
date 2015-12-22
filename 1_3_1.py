import math
import sys


TEST_SETS = [
  ['4' , '4 -8 6 0', '-10 3 1 1', '0 1'],
  ['3' , '1 6 5', '1 3 5', '1 2'],
  ['4' , '4 4 5 5', '-10 4 3 5', '2 3'],
  ['4' , '-1 -2 -3 -4', '-5 -2 -1 -2', '0 2'],
  ['4' , '5 0 10 20', '0 40 0 30', '3 3'],
  ['6' , '1 1 1 7 1 10', '1 10 1 1 7 1', '3 4'],
] 


def main(*args):
    arr_i = arr_j = 0
    arr_a = args[1].split(' ')
    arr_b = args[2].split(' ')
    maxs = []
    max_i = [0, 0]
    max_sum = sum([int(arr_a[max_i[0]]), int(arr_b[max_i[1]])])
    while arr_i < int(args[0]):
        arr_j = arr_i
        while arr_j < int(args[0]):
          num_a = int(arr_a[arr_i])
          num_b = int(arr_b[arr_j])
          cur_sum = sum([num_a, num_b])
          if cur_sum > max_sum:
              max_sum = cur_sum
              max_i = [arr_i, arr_j]
          arr_j += 1
        arr_i += 1
    return ' '.join([str(i) for i in max_i])


def test():
    result = True
    for i in TEST_SETS:
        if main(*i[:3]) != i[3]:
            result = False
            print(main(*i[:3]), ' != ' , i[3])
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        print("Test - ", test() and 'Ok')
    else:
        arr_len = input()
        arr_a = input()
        arr_b = input()
        print(main(arr_len, arr_a, arr_b))
