__author__ = 'bj'

from random import randint

test1 = [1, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3, 7]
test2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
test3 = [2, 7, 1, 8, 2, 8, 1]
test4 = []
test5 = [3]
test6 = ["abc"]
test7 = [2, 2, 2, 2, 2, 2, 2]
test8 = ["a", "b", "c", "b"]

test_suite = [test1, test2, test3, test4, test5, test6, test7, test8]


def find_longest_length(seq, best_len=0, curr_len=0, last=None):
    """
    Identify the length of the longest incrementing sub-sequence
    :type seq: list
    :type best_len: int
    :type curr_len: int
    :type last: int
    """
    if seq == []:
        return best_len
    elif last is not None and seq[0] > last:
        if curr_len == 0:
            curr_len = 1
        curr_len += 1
        if curr_len > best_len:
            best_len = curr_len
        return find_longest_length(seq[1:], best_len, curr_len, seq[0])
    else:
        return find_longest_length(seq[1:], best_len, 0, seq[0])

def fll_non_recursive(seq):
    best_len, curr_len = 0, 0
    if seq:
        last = seq[0]
        for x in seq[1:]:
            if last < x:
                if curr_len == 0: curr_len = 1
                curr_len += 1
            else:
                if curr_len > best_len: best_len = curr_len
                curr_len = 0
            last = x
    return best_len


test_fun = fll_non_recursive

for test in test_suite:
    print(test_fun(test), " : ", test)

test = []
for x in range(1000):
    test.append(randint(0,1000))
print(test_fun(test), " : 1,000 integer list")
