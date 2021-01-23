# Given an list , use bucket sort to sort the elements of the list and return
#  Input: [1, 2, 4, 3, 5]
#  Output: [1, 2, 3, 4, 5]

# divide the elements into several lists known as buckets
# loop through each buckets and sort them(insertion/quick sort)
# return each element of the buckets since they would be sorted already

# when the number of elements in each bucket is 1 the time complexity practically becomes n 
# very fast when the difference of elements in a list is small but with a loss at space complexity


def do_bucket_sort(nums: list) -> list:
    buckets = []
    list_len = len(nums)
    nums_indx = 0
    for i in range(list_len+1):
        buckets.append([])
    
    for i in nums:
        buckets[i].append(i)
        buckets[i].sort()

    for bucket in buckets:
        for el in bucket:
            nums[nums_indx] = el
            nums_indx += 1
    
    return nums


def main():
    example_list = [1, 2, 4, 3, 5]
    print(do_bucket_sort(example_list))


if __name__ == "__main__":
    main()
