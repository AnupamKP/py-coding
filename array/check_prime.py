'''
Check whether a number is a prime number or not!

Input: 25
Output: False
'''
import math
def check_prime(num: int) -> int:
    end = int(math.sqrt(num)) + 1

    for i in range(2, end):
        if num % i == 0:
            return False

    return True

if __name__ == "__main__":
    num = 25
    print(check_prime(num))