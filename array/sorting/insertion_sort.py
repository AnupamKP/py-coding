# Given an list , use insertion sort to sort the elements of the list and return
#  Input: [1, 2, 4, 3, 5]
#  Output: [1, 2, 3, 4, 5]

# divide the list into left and right list
# if el at right is smaller than left array last element ,
# then bring the el from right and sort it in left array


def do_insertion_sort(nums: list) -> list:
    list_len = len(nums)
    for right_list_index in range(1, list_len):
        new_el = nums[right_list_index]
        left_list_index = right_list_index - 1

        while(left_list_index >= 0 and new_el < nums[left_list_index]):
            nums[left_list_index + 1] = nums[left_list_index]
            left_list_index -= 1

        nums[left_list_index + 1] = new_el

    return nums


def main():
    example_list = [1, 2, 4, 3, 5]
    print(do_insertion_sort(example_list))


if __name__ == "__main__":
    main()
