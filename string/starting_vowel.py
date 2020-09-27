'''
You are given a string S, and you have to find all the substrings of S that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input
Only argument given is string S.

Output
Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.

Example:

Input
    ABEC

Output
    6

Explanation
	Amazing substrings of given string are :
	1. A
	2. AB
	3. ABE
	4. ABEC
	5. E
	6. EC
	here number of substrings are 6 and 6 % 10003 = 6.


'''

def nu_of_substring_starting_with_vowels(A: str) -> int:
    result = 0

    for i in range(len(A)):
        if A[i].lower() in ['a','e', 'i', 'o', 'u']:
            result += (len(A) - i)
        
        
    return result % 10003

if __name__ == "__main__":
    A = "ABEC"
    print(nu_of_substring_starting_with_vowels(A))
