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
] 


TEST_SETS_GET_INDEXES = [
    {'num': 2, 'result': [0, 1]},
    {'num': 4, 'result': [1, 2]},
]


TEST_SETS_DIFF = [
    {'index': 2, 'arr': [10,20,30], 'num': 25, 'result': 5},
    {'index': 1, 'arr': [10,20,30], 'num': 25, 'result': 5},
]


def get_indexes(num, result=None):
    num = int(num)
    return [num // 2 - 1, num // 2]


def diff(index, arr, num, result=None):
    return abs(int(arr[index]) - int(num))


def bin_search(len_, arr, num):
    last_index = int(len_) - 1
    cur_diff = lambda x: diff(x, arr, num)
    indexes = get_indexes(last_index)
    while indexes[0] >= 0 and indexes[1] <= last_index:
        next_index = indexes[not cur_diff(indexes[0]) > cur_diff(indexes[1])]
        # import pdb; pdb.set_trace()
        result = next_index
        indexes = get_indexes(next_index)
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
            test(TEST_SETS_DIFF, diff),
            test(TEST_SETS, main)
        ]
        for i in tests:
            print_test(i)
    else:
        args = ['lena', 'arra', 'lenb', 'arrb']
        inputs = {}
        for i in args:
            inputs[i] = input('Input %s: ' % i)
        print(main(**inputs))
