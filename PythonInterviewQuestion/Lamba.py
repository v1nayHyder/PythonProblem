# s=lambda a,b:a+b
# print(s(4,5))
# print((lambda a,b:a+b)(3,4))
# val=(lambda a,b:a*b)(5,6)
# print(val)
# l=[1,3,2,6,5]
# l1=list(filter(lambda x:x%2==0,l))
# print(l)
# print(l1)
# l=[10,20,30,40,50]
# sum=reduce
# Define the decorator
# def simple_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper
#
# # Use the decorator
# @simple_decorator
# def my_function():
#     print("The function is running")
#
# # Call the decorated function
# my_function()

def decor(func):
   def inner(name):
    if name=="Sunny":
       print("Hello Sunny Bad Morning")
    else:
        func(name)
    return inner

@decor
def wish(name):
 print("Hello",name,"Good Morning")

wish("Durga")
# 14) wish("Ravi")
# 15) wish("Sunny")