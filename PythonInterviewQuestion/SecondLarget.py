def find_second_largest(nums:list)->int:
    if len(nums)<2:
        return -1
    largest=0
    second_largest=largest
    for val in nums:
        second_largest = val
        if second_largest > largest:
            second_largest ,largest = largest,second_largest
    return second_largest

list=[1,4,3,6,7,7,6]
second_largest=find_second_largest(list)
print(second_largest)