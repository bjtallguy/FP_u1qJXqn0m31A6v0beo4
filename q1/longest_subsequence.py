__author__ = 'bj'


def find_longest_inc_subsequence(seq):
    """Solution for Q1
    Given an unordered array of integers of length N > 0, calculate the length of
    the longest ordered (ascending from left [lower index] to right [higher index])
    sub-sequence within the array.

    * Recursive, functional and binary-search solutions have already been rejected.
    """

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


if __name__ == '__main__':
    """Basic demonstration - Note: See tests directory for unit tests
    """
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

    for test in test_suite:
        print(find_longest_inc_subsequence(test), " : ", test)

    test = []
    for i in range(10**6):
        test.append(randint(0, 1000))
    print(find_longest_inc_subsequence(test), " : ", len(test), " integer list")
