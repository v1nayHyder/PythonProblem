def is_sorted_list(nums:list)->bool:
    for index in range(len(nums)-1):
        if nums[index]>nums[index+1]:
            return False

    return True


nums=[1,2,4,3,4,6]
is_sorted=is_sorted_list(nums)
print(is_sorted)