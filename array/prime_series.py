'''
Generate a series of prime number till a given number. Hint: SieveOfErathothenes

Input: 50
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

'''

def generate_prime_num(num: int) -> list:
    prime = [True for i in range(num + 1)]
    p = 2
    while(p * p <= num):
        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    result = []
    for i in range(2, num + 1):
        if prime[i]:
            result.append(i)

    return result

if __name__ == "__main__":
    num = 50
    print(generate_prime_num(num))