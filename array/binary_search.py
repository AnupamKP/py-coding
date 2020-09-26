'''
Given an sorted integer array , implement a binary search to find an integer index in the array.

If the key is not present , return -1

Input:
    A = [1,2,3,4,5]
    3

Output:
    2

'''

def do_binary_search(A: list, key: int) -> int:
    left = 0
    right = len(A)
    while (right > left):
        mid = (left + right)//2
        if key == A[mid]:
            return mid
        else:
            if key > mid:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1



if __name__ == "__main__":
    A = [1,2,3,4,5]
    key = 3
    print(do_binary_search(A,key))