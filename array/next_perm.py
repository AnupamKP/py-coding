'''
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.
If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

Constraints:

1 <= N <= 5e5
1 <= A[i] <= 1e9


Input 1:
    A = [1, 2, 3]

Output 1:
    [1, 3, 2]

Input 2:
    A = [3, 2, 1]

Output 2:
    [1, 2, 3]

'''

def next_permutation(A: list) -> list:
    # Using Narayana Pandita algorithm
    k = -1
    # Step 1: find max k such that A[k]<A[k+1]
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            k = i
    # if no max k found , return reverse list
    if k == -1:
        return A[::-1]
    else:
        # Step 2: find l such that A[l]>A[k]
        for j in range(k+1, len(A)):
            if A[j] > A[k]:
                l = j
        # Step 3: swap A[l] and A[k]
        A[l], A[k] = A[k], A[l]
        # Step 4: reverse k+1 to end
        A[k+1:len(A):1] = A[len(A)-1:k:-1]
        return A

if __name__ == "__main__":
    A = [1, 2, 3]
    print(next_permutation(A))
