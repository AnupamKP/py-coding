'''
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]

'''

def get_all_subsets(A: list) -> list:
    list_of_subsets=[]
    A.sort()

    def get_subsets(A: list, subset: list, index: int) -> None:
        list_of_subsets.append(subset[:])
        for i in range (index, len(A)):
            subset.append(A[i])
            get_subsets(A, subset, i+1)
            subset.pop(-1)
        return

    get_subsets(A, [], 0)
    return list_of_subsets

if __name__ == "__main__":
    A = [1,2,3]
    print(get_all_subsets(A))