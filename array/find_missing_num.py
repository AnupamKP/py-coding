'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.

'''


def find_first_missing_number(A: list) -> int:
    # Set all the -ve and extra num as len(A) + 1
    for i, item in enumerate(A):
        if item < 0 or item > len(A):
            A[i] = len(A) + 1

    for item in A:
        item = abs(item)
        # skip extra number what we updated in 1st pass
        if item == len(A) + 1:
            continue
        # if num index is pos(not visited) , make it negative(visited)
        if A[item - 1] > 0:
            A[item - 1] *= -1

    # find the pos(not visited) number
    for j, item in enumerate(A):
        if item > 0:
            return j+1

    return len(A) + 1

if __name__ == "__main__":
    A = [1,2,0]
    print(find_first_missing_number(A))