"""N glasses of capacity 1, ... , N . what is the minimum number of glasses needed
to pour K liters."""


# solution draft, does not work for all cases
def solution(N: int, K:int) -> int:
    # Implement your solution here

    if K <= N:
        return 1
    else:
        # array of glasses
        glasses = [n for n in range(1, + N+1)]
        sum_glasses = []
        sum_ = 0
        for n in glasses:
            sum_ += n
            sum_glasses.append(sum_)
        if K in sum_glasses:
            for i, s in enumerate(sum_glasses):
                if K == s:
                    return i + 1
        elif K > sum_glasses[-1]:
            return -1
        elif K - N in glasses:
            return 2
    return -1

# optimal solution from GPT
def min_glasses_needed(N: int, K: int) -> int:
    # Calculate the total capacity of all glasses
    total_capacity = N * (N + 1) // 2

    # If K is greater than the total capacity, it's not possible
    if K > total_capacity:
        return -1

    # Start with the largest glasses first
    glasses = list(range(N, 0, -1))  # Glasses with capacities N, N-1, ..., 1
    count = 0

    for glass in glasses:
        if K == 0:
            break
        # Use as many of the current glass as possible
        count += K // glass
        K %= glass

    return count

if __name__ == "__main__":

    print(solution(10, 0))
    print(min_glasses_needed(10, 0  ))