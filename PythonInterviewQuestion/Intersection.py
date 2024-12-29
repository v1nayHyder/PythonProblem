def intersection(nums1:list,nums2:list)->list:
    new_list=[]
    for num in nums1:
        if num in nums2:
            new_list.append(num)
            nums2.remove(num)
    return  new_list


nums1=[1,2,3,4,2]
nums2=[2,3,6,7,4,2]
inter_list=intersection(nums1,nums2)
print(inter_list)