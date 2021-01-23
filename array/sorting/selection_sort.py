# Given an list , use selection sort to sort the elements of the list and return
#  Input: [1, 2, 4, 3, 5]
#  Output: [1, 2, 3, 4, 5]

#Find min/max for ascending/descending and swap with the number present in that position


def do_selection_sort(nums: list) -> list:
    list_len = len(nums)
    for i in range(list_len):
        min_indx = i
        for j in range(i+1,list_len):
            if nums[j] < nums[min_indx]:
                min_indx = j
        nums[i],nums[min_indx] = nums[min_indx],nums[i]
    
    return nums

def main():
    example_list = [1, 2, 4, 3, 5]
    print(do_selection_sort(example_list))


if __name__ == "__main__":
    main()
