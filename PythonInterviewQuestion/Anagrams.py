def is_anagram(str1:str,str2:str)->bool:
    if len(str1) !=len(str2):
        return False
    # return sorted(str1)==sorted(str2)
    # for char in str1:
    #     if char not in str2:
    #         return False
    # return True
    dict1={}
    dict2={}
    for x in str1:
        if x in dict1:
            dict1[x]=dict1[x]+1
        else:
            dict1[x]=1
    for x in str2:
        if x in dict2:
            dict2[x] = dict2[x] + 1
        else:
            dict2[x] = 1
    return dict1==dict2



str1="alisten2a"
str2="silent2a"
isAnagrma=is_anagram(str1,str2)
print(isAnagrma)