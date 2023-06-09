'''
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.

Input Format
First and only argument is an integer array A.

Output Format
Return 1 if any such integer p is found else return -1.

Input 1:

 A = [3, 2, 1, 3]

Output 1:

 1

'''


def is_noble_integer(A: list) -> int:
    A.sort()
    end = len(A)
    # edge case when 0 is the max int and all other are -ve
    if A[-1] == 0:
        return 1

    for i in range(end-1):
        rem_len = end - (i+1)
        if A[i] != A[i+1] and rem_len == A[i]:
            return 1

    return -1


if __name__ == "__main__":
    A = [3, 2, 1, 3]
    print(is_noble_integer(A))
