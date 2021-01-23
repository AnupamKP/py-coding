'''
Q. Given a string with different set of parenthesis , write a function to test whether the parenthesis order are correct or not.

Input: '{[()]}'
Output: True

Input: '{[()]]}'
Ouput: False
'''

def isValid(s: str) -> bool:
    stack = []
    lookup = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    for c in s:
        if stack and c in lookup.keys() and stack[-1] == lookup[c]:
            stack.pop(-1)
        else:
            stack.append(c)
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    input = '{[()]}'
    print(isValid(input))