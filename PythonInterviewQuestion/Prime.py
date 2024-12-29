
#program to check if a number is a prime or not
def is_prime_number(num:int)->bool:
    if num<2:
        return False

    for val in range(2,num):
        if num%val==0:
            return False

    return True


num=0

is_prime=is_prime_number(num)

print(is_prime)