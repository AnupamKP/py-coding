'''
You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

'''


def repeated_number(A: list) -> int:
    req_times = len(A)//3
    count_map = {}
    for item in A:
        count_map[item] = count_map.get(item, 0) + 1

    for item_key, item_val in count_map.items():
        if item_val > req_times:
            return item_key

    return -1


if __name__ == "__main__":
    A = [1, 2, 3, 1, 1]
    print(repeated_number(A))
