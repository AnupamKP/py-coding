'''
Given a string A consisting of lowercase characters.

We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.


Example Input

Input 1:
    A = "abede"
Input 2:
    A = "aabb"


Example Output

Output 1:
    2
Output 2:
    2
 '''

def min_append_to_palindrome(A: str) -> int:
    len_A = len(A)
    for i in range(len_A):
        temp_str = A[i:]
        if temp_str == temp_str[::-1]:
            return len_A - (len_A - i)
        
    return 1

if __name__ == "__main__":
    A = "aabb"
    print(min_append_to_palindrome(A)) 