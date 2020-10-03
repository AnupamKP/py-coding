'''
The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive integer that perfectly divides the two given numbers. 
For example, the H.C.F of 12 and 14 is 2.

Given two numbers find the gcd.

Input:

A = 12
B = 14

Output:

2

'''

def gcd(A: int, B:int) -> int:
    # Using Euclidean Algorithm
    while B != 0:
        A,B = B,A%B
    return A

if __name__ == "__main__":
    A = 300
    B = 400
    print(gcd(A,B))