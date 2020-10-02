'''
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]

NOTE:
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.

'''

def get_all_permutations(A: list) -> list:
    result = []
    def get_permutations(arr: list, prefix: list, result: list) -> None:
        if len(arr) == 0:
            result.append(prefix[:])
        else:
            for i in range(len(arr)):
                get_permutations(arr[:i] + arr[i + 1:], prefix + [arr[i]], result)
    
    get_permutations(A, [], result)
    return result

if __name__ == "__main__":
    A = [1,2,3]
    print(get_all_permutations(A))
