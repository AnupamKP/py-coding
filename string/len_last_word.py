'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.
'''

def length_of_last_word(A: str) -> int:
    word_list = A.strip().split(" ")
    return 0 if len(word_list) == 0 else len(word_list[-1])

if __name__ == "__main__":
    A = "Hello world   "
    print(length_of_last_word(A))