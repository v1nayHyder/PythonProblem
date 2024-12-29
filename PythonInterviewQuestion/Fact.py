def factorial_num(num:int)->int:
       fact_num=1
       for x in range(1,num+1,1):
           fact_num*=x
       return fact_num


num=5
fact_num=factorial_num(num)
print(fact_num)