def find_smallest_num(nums):
    sorted_nums = sorted(set(nums))
    return sorted_nums[1]

print(find_smallest_num([6,43,67,89,5,3,3,6,8]))