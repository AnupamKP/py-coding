'''
You are given a array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
'''


def repeated_and_missing_number(A: list) -> list:
    init_sum = sum(A)
    n = len(A)
    result = [0, 0]
    for item in A:
        item = abs(item)
        if A[item-1] < 0:
            result[0] = item
            break
        else:
            A[item-1] *= -1

    expected_sum = (n*(n+1))//2
    actual_sum = init_sum - result[0]
    result[1] = expected_sum - actual_sum

    return result

if __name__ == "__main__":
    A = [3,1,2,5,3]
    print(repeated_and_missing_number(A))