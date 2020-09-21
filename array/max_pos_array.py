'''
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
Find and return the required subarray.

NOTE:
If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Example Input

Input 1:

 A = [1, 2, 5, -7, 2, 3]

Output 1:

 [1, 2, 5]

Input 2:

 A = [10, -1, 2, 3, -4, 100]

Output 2:

 [100]

Input 3:

 A = [0, 0, -1, 0]

Output 3:

 [0,0]

 '''


def max_postive_array(nums: list) -> list:
    final_max = max(nums)
    temp_max = 0
    temp_result = []
    final_result = []

    for item in nums:
        temp_max += item
        temp_result.append(item)
        if item < 0:
            temp_max = 0
            temp_result = []
        else:
            if final_max < temp_max:
                final_max = temp_max
                final_result = temp_result[:]
            if final_max == temp_max and len(temp_result) > len(final_result):
                final_result = temp_result[:]

    return final_result


if __name__ == "__main__":
    A = [0, 0, -1, 0]
    print(max_postive_array(A))
