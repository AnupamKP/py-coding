'''
Given a array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
'''

def find_duplicate(A: list) -> int:
    result = -1
    for item in A:
        item = abs(item)
        if A[item-1] < 0:
            return item
        else:
            A[item-1] *= -1

    return result

if __name__ == "__main__":
    A = [3,4,1,4,1]
    print(find_duplicate(A))
