'''
Given a number A. Find the fatorial of the number.

Problem Constraints
1 <= A <= 100

'''

def factorial(n,memorize = {1:0 , 2:1}):
        if n in memorize:
                return memorize[n]
        else:
                memorize[n] = facrorial(n-1,memorize)+ factorial(n-2,memorize)
                return memorize[n]

if __name__ == "__main__":
    A = 3
    print(factorial(A))
