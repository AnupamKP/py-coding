'''
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"


Return a + b = “111”.
'''

def get_binary_sum(A: str, B: str) -> str:
    return bin(int(A,base=2)+int(B,base=2))[2:]

if __name__ == "__main__":
    print(get_binary_sum("11","100"))