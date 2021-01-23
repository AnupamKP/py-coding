# Given an list , use merge sort to sort the elements of the list and return
#  Input: [1, 2, 4, 3, 5]
#  Output: [1, 2, 3, 4, 5]

# get the middle element
# create two lists from the main list into left and right list
# compare left and right list and push the min el into the main list
# push the remaining left or right list elements when the left and right are uneven.

def do_merge_sort(nums: list) -> list:
    list_len = len(nums)
    if list_len > 1:
        mid_indx = list_len // 2
        left_list, right_list = nums[:mid_indx], nums[mid_indx:]

        do_merge_sort(left_list)
        do_merge_sort(right_list)

        i = j = k = 0

        while(i < len(left_list) and j < len(right_list)):
            if left_list[i] <= right_list[j]:
                nums[k] = left_list[i]
                i += 1
            else:
                nums[k] = right_list[j]
                j += 1
            k += 1

        while(i < len(left_list)):
            nums[k] = left_list[i]
            i += 1
            k += 1

        while(j < len(right_list)):
            nums[k] = right_list[j]
            j += 1
            k += 1


def main():
    example_list = [1, 2, 4, 3, 5]
    do_merge_sort(example_list)
    print(example_list)


if __name__ == "__main__":
    main()
