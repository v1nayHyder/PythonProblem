# from sys import argv
# for x in argv:
#     print(x,end=" ")
# num=int(input("Enter number:"))
# for val in range(1,num+1):
#     for x in range(1,val+1):
#         print("*",end=" ")
#     print()
# string="Vinay"
# print(string.find("inay"))
name="Vinay prakash yadav"
dic={}
for word in name:
    print(word)
    if word in dic.keys():
        dic[word.lower()]=dic[word.lower()]+1
    else:
        dic[word.lower()]=1

print(dic)