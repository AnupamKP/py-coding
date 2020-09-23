'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Input : [1, 10, 5]
Output : 5 
'''
def maximum_consecutive_difference(A: list) -> int:
        if len(A) < 2:
            return 0

        A.sort(reverse=True)
        max_diff = A[0] - A[1]
        for i in range(len(A)-1):
            temp_diff = A[i] - A[i+1]
            max_diff = max(temp_diff,max_diff)
        
        return max_diff

if __name__ == "__main__":
    A = [1, 10, 5]
    print(maximum_consecutive_difference(A))