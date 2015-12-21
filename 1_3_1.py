import math
import sys


TEST_SETS = [
  ['4' , '4 -8 6 0', '-10 3 1 1', '0 1'],
  ['3' , '1 6 5', '1 3 5', '1 2'],
  ['4' , '4 4 5 5', '-10 4 3 5', '2 3'],
  ['4' , '-1 -2 -3 -4', '-5 -2 -1 -2', '0 2'],
  ['3' , '5 0 10 20', '0 40 0 30', '2 2'],
] 


def check(next, n_index, current, c_index, partner, p_index):
    if int(next) >= int(current):
        
     

def main(*args):
    arr_i = int(args[0]) - 1
    arr_a = args[1].split(' ')
    arr_b = args[2].split(' ')
    max_a = [int(arr_a[-1]), arr_i]
    max_b = [int(arr_b[-1]), arr_i]
    while arr_i > 0:
        arr_i -= 1        
        arr_a[arr_i] = int(arr_a[arr_i])
        arr_b[arr_i] = int(arr_b[arr_i])
        if arr_b[arr_i] >= max_b[0] and ((arr_b[arr_i] - max_b[0]) >= max_a[0]):
            max_b = [arr_b[arr_i], arr_i]
            max_a = [arr_a[arr_i], arr_i]
            continue
        if arr_a[arr_i] >= max_a[0]:
            max_a = [arr_a[arr_i], arr_i]
    return ' '.join([str(max_a[1]), str(max_b[1])])


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
