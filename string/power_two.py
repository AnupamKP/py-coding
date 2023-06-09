'''
Find if Given number is power of 2 or not.

NOTE: return 1 if the number is a power of 2 else return 0

Example:

Input : 128
Output : 1

'''

def is_power_of_two(A: str) -> int:
    '''
    Concept: A binary number which is a power of 2 will always have only one 1. 
    (Example: 010,100,1000,..)
    '''
    A = int(A)
    binary_num = bin(A)
    
    if A == 1:
        return 0
    
    if binary_num.count('1') > 1:
        return 0
    else:
        return 1

if __name__ == "__main__":
    A = "128"
    print(is_power_of_two(A))