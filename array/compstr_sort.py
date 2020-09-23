'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

from functools import cmp_to_key
def comparestr_sort(A: list) -> str:
    def custom_compare(num1: int, num2:int) -> int:
        left_val = int(str(num1)+str(num2))
        right_val = int(str(num2)+str(num1))

        if left_val > right_val:
            return -1
        else:
            return 1

    A.sort(key=cmp_to_key(custom_compare))
    return "0" if A[0] == 0 else "".join(map(str,A))

if __name__ == "__main__":
    A = [8,89]
    print(comparestr_sort(A))