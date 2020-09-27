'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

def is_palindrome(A: str) -> int:
    original = []

    for c in A:
        if c.isalnum():
            original.append(c.lower())

    return 1 if "".join(original) == "".join(original[::-1]) else 0

if __name__ == "__main__":
    A = "race a car"
    print(is_palindrome(A))