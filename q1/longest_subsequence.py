__author__ = 'bj'

from random import randint

test1 = [1, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3, 7]
test2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
test3 = [2, 7, 1, 8, 2, 8, 1]
test4 = []
test5 = [3]
test6 = [2, 2, 2, 2, 2, 2, 2]
test7 = ["abc"]
test8 = ["a", "b", "c", "b"]

test_suite = [test1, test2, test3, test4, test5, test6, test7, test8]


def fll_non_recursive(seq):
    best_len = 0
    curr_len = 0
    if seq:
        last = seq[0]
        for x in seq[1:]:
            if last < x:
                if curr_len == 0:
                    curr_len = 1
                curr_len += 1
            else:
                if curr_len > best_len:
                    best_len = curr_len
                curr_len = 0
            last = x
    return best_len


for test in test_suite:
    print(fll_non_recursive(test), " : ", test)

test = []
for i in range(10**6):
    test.append(randint(0, 1000))
print(fll_non_recursive(test), " : ", len(test), " integer list")
