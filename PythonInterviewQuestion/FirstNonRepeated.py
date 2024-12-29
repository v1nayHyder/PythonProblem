def non_repeated_char(string:str):
   dict={}
   for char in string:
       if char in dict:
           dict[char]=dict[char]+1
       else:
           dict[char]=1;
   for char in dict:
       if dict[char]==1:
           return char

   return None


string="swisswi"
ch_one_occurrence=non_repeated_char(string)
print(ch_one_occurrence)