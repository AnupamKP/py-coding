'''
Given a number A. Find the fatorial of the number.

Problem Constraints
1 <= A <= 100

'''

def factorial(A: int) -> int:
        if A <= 1:
            return 1

        return (A * factorial(A-1))

if __name__ == "__main__":
    A = 3
    print(factorial(A))