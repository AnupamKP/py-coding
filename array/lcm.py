'''
LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers. 

For example, LCM of 15 and 20 is 60, and LCM of 5 and 7 is 35.

Input:

A = 15
B = 60

Output:

60

Hint:
LCM * GCD = A * B
'''

from gcd import gcd

def lcm(A:int, B:int) -> int:
    return (A * B)//gcd(A,B)

if __name__ == "__main__":
    A = 5
    B = 7
    print(lcm(A,B))