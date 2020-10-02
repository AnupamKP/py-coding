'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Input: S = "ab#c", T = "ad#c"
Output: True
Input: S = "ab##", T = "c#d#"
Output: True
'''



def bksp_compare_strings(string1:str , string2:str) -> bool:
    
    def get_actual_string(input_string:str) -> str:
        num_of_bsp = 0
        response_string = ""
        for c in input_string[::-1]:
            if c == "#":
                num_of_bsp += 1
            else:
                if num_of_bsp > 0:
                    num_of_bsp -= 1
                else:
                    response_string += c
        return response_string

    return (get_actual_string(string1) == get_actual_string(string2))

if __name__ == "__main__":
    S = "ab#c"
    T = "ad#c"
    print(bksp_compare_strings(S,T))