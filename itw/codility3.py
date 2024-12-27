"""Given the binary representation in the form of a string containing only 0s and 1s,
return the number of steps to reduce it to 0 using a Syracuse-like algorithm: if it is even,
divide it by 2, if it is odd, substract 1, until u reach 0."""

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

    print(f"number = {V}")
    count = 0
    while V > 0 :
        if V % 2 == 0 :
            V = V // 2
        else:
            V -= 1
        count +=1

    return count

if __name__ == '__main__':

    S = '1000'
    #for i in range(400000):

   #     S += '1'

    print(solution(S))