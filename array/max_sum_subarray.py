'''
Find the contiguous subarray within an array, A of length N which has the largest sum.

1 <= N <= 1e6
-1000 <= A[i] <= 1000


Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.

'''


def max_sum_subarray(A: list) -> int:
    final_max = max(A)
    temp_max = 0
    for item in A:
        temp_max += item
        if temp_max < 0:
            temp_max = 0
        else:
            final_max = max(final_max, temp_max)

    return final_max


if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sum_subarray(A))
