def largest_num(num_list):
    # return max(num_list)
    if len(num_list)==0:
     return None
    max=-2**31
    for num in range(len(num_list)):
        if max< num_list[num]:
            max=num_list[num]
    return max

nums_list=[]
larg_num=largest_num(nums_list)
print(larg_num)