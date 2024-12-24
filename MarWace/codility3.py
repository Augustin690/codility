# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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

    count = 0
    while V > 0 :
        if V % 2 == 0 :
            V = V // 2
        else:
            V -= 1
        count +=1

    return count

if __name__ == '__main__':

    S = ''
    for i in range(400000):

        S += '1'

    print(solution(S))