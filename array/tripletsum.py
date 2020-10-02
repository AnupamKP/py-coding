'''
Given an list and an element, find if there is a triplet in list whose sum is equal to the given element.

Input: [1, 2, 4, 3, 5]
9
Output: [1, 3, 5]

'''
def get_triplet(nums: list, el: int) -> list:
    nums.sort()
    list_len = len(nums) - 2
    result = []
    for i in range(list_len):
        first_indx,sec_indx,third_indx = i, i + 1, -1
        first_num = nums[first_indx]
        second_num = nums[sec_indx]
        third_num = nums[third_indx]
        while(first_num < third_num):
            sum = first_num + second_num + third_num
            if sum == el:
                result.append(first_num)
                result.append(second_num)
                result.append(third_num)
                return result
            elif sum < el:
                sec_indx += 1
                second_num = nums[sec_indx]
            else:
                third_indx -= 1
                third_num = nums[third_indx]

    return result

if __name__ == "__main__":
    A = [1, 2, 4, 3, 5]
    el = 9
    print(get_triplet(A,el))
