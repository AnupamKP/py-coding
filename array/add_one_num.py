'''
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
'''


def add_one_num(A: list) -> list:
    result_num = int("".join(list(map(str, A))))+1
    result = [c for c in str(result_num)]
    return result

if __name__ == "__main__":
    A = [1,2,3]
    print((add_one_num(A)))
