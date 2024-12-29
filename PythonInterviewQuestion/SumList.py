#program to calculate sum of element in list
def sum_of_list(nums:list)->int:
      total_sum=0

      for num in nums:
          total_sum+=num
      return total_sum

nums=[1, 2, 3, 4, 5]
total_sum=sum_of_list(nums)
print(total_sum)
