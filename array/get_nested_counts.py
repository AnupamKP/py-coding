'''
Given an nested list with unknown depth with only elements as 0 or 1.
Find the count of total zeroes and ones and return it as tuple.

Input:
[0, 0, [0, 0, 0, 0, 1, [1, 1, [0, [0, 0, 1, 1], 0, 1, 1], 1]], 0, 1, [0, 0, 0, 1, [1, 1, 1]], 1]

Output:
(14,14)

'''


def get_nested_counts(original_list:list) -> tuple:
    zero_counter = 0
    one_counter = 0
    def loop_each_element(temp_list: list) -> None:
        nonlocal zero_counter
        nonlocal one_counter

        for idx,element in enumerate(temp_list):
            if type(element) == int:
                if element == 1:
                    one_counter += 1
                else:
                    zero_counter += 1
            else:
                loop_each_element(element)
        
        return 


    loop_each_element(original_list)

    return (zero_counter,one_counter)


if __name__ == "__main__":
    lst = [0, 0, [0, 0, 0, 0, 1, [1, 1, [0, [0, 0, 1, 1], 0, 1, 1], 1]], 0, 1, [0, 0, 0, 1, [1, 1, 1]], 1]

    print(get_nested_counts(lst))