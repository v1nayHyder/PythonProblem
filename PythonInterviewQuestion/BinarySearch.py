
def find_target(nums:list,target:int)->int:
    if len(nums)==0:
        return -1
    left,right=0,len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1

nums=[1,2,3,4,5,5,7,8,9]
target=9
result=find_target(nums,target)
print(result)