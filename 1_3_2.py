import math
import sys


"""
Дан отсортированный массив различных целых чисел A[0..n-1] и массив целых чисел B[0..m-1].
Для каждого элемента массива B[i] найдите минимальный индекс элемента массива A[k],
ближайшего по значению к B[i].
Время работы поиска для каждого элемента B[i]: O(log(k)).
Подсказка. Обратите внимание, что время работы должно зависеть от индекса ответа - k. 
Для достижения такой асимптотики предлагается для начала найти отрезок вида [2p,2p+1] , 
содержащий искомую точку, а уже затем на нём выполнять традиционный бин. поиск.

Sample Input:
3
10 20 30
3
9 15 35

Sample Output:
0 0 2
"""


TEST_SETS = [
  {'lena': '3' , 'arra': '10 15 35', 'lenb': '3','arrb': '5 7 30', 'result': '0 0 2'},
  {'lena': '3' , 'arra': '10 20 30', 'lenb': '3','arrb': '9 15 35', 'result': '0 0 2'},
  {'lena': '3' , 'arra': '-10 5 20', 'lenb': '3','arrb': '-15 15 0', 'result': '0 2 1'},
  {'lena': '3' , 'arra': '-10 -10 -1', 'lenb': '3','arrb': '-15 16 0', 'result': '0 2 2'},
  {'lena': '3' , 'arra': '-10 0 5', 'lenb': '3','arrb': '-7 1 5', 'result': '0 1 2'},
  {'lena': '3' , 'arra': '0 0 15', 'lenb': '3','arrb': '0 0 11', 'result': '0 0 2'},
  {'lena': '4' , 'arra': '-15 -5 -1 2', 'lenb': '4','arrb': '5 -6 -11 0', 'result': '3 1 0 2'},
  {'lena': '5' , 'arra': '10 15 35 35 50', 'lenb': '5','arrb': '10 7 40 20 30', 'result': '0 0 2 1 2'},
] 


TEST_SETS_GET_INDEXES = [
    {'num': 2, 'result': [0, 1]},
    {'num': 4, 'result': [1, 2]},
]


def noresult(func):
    def wrapper(*args, **kwargs):
        if 'result' in kwargs.keys():
            del kwargs['result']
        return func(*args, **kwargs)
    return wrapper


@noresult
def get_indexes(num):
    num = int(num)
    if num > 1:
        return [num // 2 - 1, num // 2]
    else:
       return [0, 1]


@noresult
def diff(index, arr, num):
    return abs(int(arr[index]) - int(num))


@noresult
def new_diff(arr, num, i, j):
    i, j, num = (int(arr[i]), int(arr[j]), int(num))
    result = False
    diff_i, diff_j = (num - i, j - num)
    if i == j and i > 0:
        pass
    elif diff_j < 0 or diff_i > diff_j:
        result = True
        # if num == 40:
        #     import pdb; pdb.set_trace()
    return result


def bin_search(len_, arr, num):
    last_index = int(len(arr)) - 1
    cur_diff = lambda x, y: diff(x, y, num)
    indexes = get_indexes(last_index)
    offset = 0
    while len(arr) >= 2:
        index = new_diff(arr, num, *indexes)
        next_index = indexes[index]
        if index:
            offset += (lambda: 0 if len(arr) <= 2 else indexes[1])()
            arr = arr[indexes[1]:]
        else:
            arr = arr[:indexes[1]]
        result = next_index + offset
        indexes = get_indexes(len(arr) - 1)
    return result


def main(lena, arra, lenb, arrb, result=None):
    arra = arra.split(' ')
    arrb = arrb.split(' ')
    result = ''
    for i in arrb:
        result += str(bin_search(lena, arra, i))
    return ' '.join([str(i) for i in result])


def test(test_sets, func):
    success = True
    for i in test_sets:
        result = func(**i)
        if result != i['result']:
            success = False
            print(result, ' != ' , i['result'])
    return success


def print_test(result):
    print("Test - ", result and 'Ok')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        tests = [
            test(TEST_SETS_GET_INDEXES, get_indexes),
            test(TEST_SETS, main)
        ]
        for i in tests:
            print_test(i)
    else:
        args = ['lena', 'arra', 'lenb', 'arrb']
        inputs = {}
        for i in args:
            inputs[i] = input()
        print(main(**inputs))
