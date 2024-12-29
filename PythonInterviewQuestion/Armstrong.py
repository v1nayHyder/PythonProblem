# def armstrong_number(num):
#     sum=0;
#     temp=num
#     while num>0:
#         rem=num%10
#         sum+=(rem**3)
#         num//=10
#     return sum==temp
#
#
#
# number=153
# print(armstrong_number(number))
from fastapi import  FastAPI
def is_armstrong_number(num: int) -> bool:
    num_digits = len(str(num))
    total_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** num_digits
        temp //= 10
    return total_sum == num


# Example usage
number = 154
print(is_armstrong_number(number))  # Output: False
