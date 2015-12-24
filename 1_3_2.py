import math
import sys


TEST_SETS = [
  ['4' , '4 -8 6 0', '-10 3 1 1', '0 1'],
  ['3' , '1 6 5', '1 3 5', '1 2'],
  ['4' , '4 4 5 5', '-10 4 3 5', '2 3'],
  ['4' , '-1 -2 -3 -4', '-5 -2 -1 -2', '0 2'],
  ['4' , '5 0 10 20', '0 40 0 30', '3 3'],
  ['6' , '1 1 1 7 1 10', '1 10 1 1 7 1', '3 4'],
  ['4' , '2 1 2 3', '3 2 7 1', '0 2'],
  ['10' , '4 -8 16 16 32 -6 0 56 -6 2', '-10 3 1 1 -5 4 -5 2 -1 -1', '7 7'],
  ['4' , '7 6 5 4', '3 2 4 0', '0 2'],
] 


def main(*args, lena, arra, lenb, arrb):
    arr_i = int(args[0]) - 1
    arr_a = args[1].split(' ')
    arr_b = args[2].split(' ')
    maxs = [[int(arr_b[-1]), arr_i]]
    arr_i -= 1
    while arr_i >= 0:
        num = int(arr_b[arr_i]) 
        if num >= maxs[-1][0]:
            maxs.append([num, arr_i])
        else:
            maxs.append(maxs[-1])
        arr_i -= 1
    arr_i = 1
    temp_max = maxs.pop()
    max_i = [0, temp_max[1]]
    max_sum = sum([int(arr_a[max_i[0]]), temp_max[0]])
    while arr_i < int(args[0]):
        temp_max = maxs.pop()
        sum_temp = sum([int(arr_a[arr_i]), temp_max[0]])
        if sum_temp > max_sum:
            max_sum = sum_temp
            max_i = [arr_i, temp_max[1]]
        else:
            pass
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
        inputs = {}
        inputs['lena'] = input('Input len a:')
        inputs['arra'] = input('Input array a:')
        inputs['lenb'] = input('Input len b:')
        inputs['arrb'] = input('Input array b:')
        print(main(**inputs))
