'''
Given a string word , check if it's either uppercase, lowercase or titlecase using regex

Input: 'ABC'
Output:True
Input: 'abc'
Output:True
Input: 'aBc'
Output:False
'''

import re

def check_word(word: str) -> bool:
    return True if re.fullmatch(r'[A-Z]*|.[a-z]*', word) else False


if __name__ == "__main__":
    A = "ABC"
    print(check_word(A))