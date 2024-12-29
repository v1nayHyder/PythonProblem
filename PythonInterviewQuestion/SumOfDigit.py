def digit_sum(num:int)->int:
    sum=0
    while num>0:
        sum+=num%10
        num//=10
    return sum



num=1234
total_sum=digit_sum(num)
print(total_sum)