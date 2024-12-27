"""Given the binary representation in the form of a string containing only 0s and 1s,
return the number of steps to reduce it to 0 using a Syracuse-like algorithm: if it is even,
divide it by 2, if it is odd, subtract 1, until u reach 0.
Write an efficient algorithm to solve the problem."""


def solution(S):
    # Implement your solution here

    # first, compute V
    V = 0
    read_index = len(S) - 1
    for digit in S:
        if digit == '0':
            V = V
        elif digit == '1':
            V += 2**read_index
        read_index -= 1

    # Computing the integer V from S takes O(n) time and consumes too much memory
    # would cause problems for large numbers

    print(f"number = {V}")
    count = 0
    while V > 0 :
        if V % 2 == 0 :
            V = V // 2
        else:
            V -= 1
        count +=1

    return count

# memory optimized solution, that does not convert the number to decimal
def solution_optim(S):
    count = 0
    index = len(S) - 1

    # binary representation contains useful info: if the last bit is 1, number is odd, if its 0, number is even.
    # Start from the rightmost bit and process the binary number directly
    while index >= 0:
        if S[index] == '0':
            # If it's a zero, it means the number is even. Corresponds to division by 2 in the algorithm.
            count += 1
            index -= 1
        else:
            # If it's a one:
            # Case 1: If it's the last bit, just subtract 1 (and we're done, reached 0).
            if index == 0:
                count += 1
                break
            # Case 2: Otherwise, we have an odd number. We
            while index >= 0 and S[index] == '1':
                count += 1  # Subtract 1
                index -= 1
                # Add 1 for the division after turning trailing ones into zero
                if index >= 0:  # Accounting for the division after we made the number even
                    count += 1

    return count

# memory optimized solution, that does not convert the number to decimal
def solution_optim2(S):
    count = 0
    index = len(S) - 1

    # Convert the binary string to a list for easy modification
    S = list(S)

    # binary representation contains useful info: if the last bit is 1, number is odd, if its 0, number is even.
    # Start from the rightmost bit and process the binary number directly
    while index >= 0:
        # even number
        if S[index] == '0':
            # If it's a zero, it means the number is even. Corresponds to division by 2 in the algorithm:
            # we shift the index to the left. ---> '1110' = 14 -> '111' is 7
            count += 1
            index -= 1

        # odd number
        else:
            # Case 1: If it's the last bit, just subtract 1 (and we're done, reached 0).
            if index == 0:
                count += 1
                break
            # Case 2: Otherwise, we have an odd number. We subsract 1 by flipping the bit to 0, giving an even number.
            while index >= 0 and S[index] == '1':
                count += 1  # Subtract 1
                S[index] = '0'

    return count


if __name__ == '__main__':

    # = "1110"
    S = ''

    # test if implementation is memory efficient
    for i in range(400000):

        S += '1'

    print(solution_optim(S))
    #print(solution(S))