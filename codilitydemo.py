""" Given an array A, write an algorithm to find the largest strictly positive integer that is not
contained in the array."""

from typing import List

# only 1 out of 4 in performance tests, suboptimal solution
# complexity in O(max(A) * len(A))
def solution(A: List[int]) -> int:
    # Implement your solution here
    max_A = max(A)
    if max_A < 0 :
        return 1
    n = 1
    # gonna loop until maxA is reached, that can be a very large number
    while n <= max_A:
        if n not in A :
            return n
        n += 1
    return max_A + 1

# passes performance tests 4 out of 4
# complexity in 0(len(A))
def solutionGPT(A: List[int]) -> int:
    # Filter to keep only positive integers and remove duplicates, O(len(A))
    positive_numbers = set(filter(lambda x: x > 0, A))

    # Start looking for the smallest positive integer
    smallest_missing = 1

    # Check for the smallest missing positive integer. set lookup is O(1)
    while smallest_missing in positive_numbers:
        smallest_missing += 1

    return smallest_missing

if __name__ == '__main__':

    #A = [1, 3, 6, 4, 1, 2]

    #A = [1, 2, 3]

    A = [1, 2, 3, 5]

    print(solution(A))