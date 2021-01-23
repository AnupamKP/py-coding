# Given an list , use bubble sort to sort the elements of the list and return
#  Input: [1, 2, 4, 3, 5]
#  Output: [1, 2, 3, 4, 5]

# Check two adjacent elements , swap if the second el is smaller than the first
# loop through the checks , at each loop the last element will be sorted!
# if no sorting happend in a loop , break out and return 


def do_bubble_sort(nums: list) -> list:
    list_len = len(nums)
    for i in range(list_len):
        swap = 0
        for j in range(list_len-i-1):
            if nums[j+1] < nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swap += 1
        if swap == 0:
            break
    return nums


def main():
    example_list = [1, 2, 4, 3, 5]
    print(do_bubble_sort(example_list))


if __name__ == "__main__":
    main()
