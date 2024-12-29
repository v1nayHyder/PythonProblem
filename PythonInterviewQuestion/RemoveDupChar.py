# # Program to extract and print unique characters from a string
# input_string = "ABCDABBCDABBBCCCDDEEEF"
# unique_chars = set()
#
# # Add each character to the set of unique characters
# for char in input_string:
#     unique_chars.add(char)
#
# # Join the set of unique characters into a single string
# result_string = ''.join(unique_chars)
#
# # Print the result
# print(result_string)

# Program to extract and print unique characters from a string
input_string = "ABCDABBCDABBBCCCDDEEEF"
unique_chars = set(input_string)  # Directly create a set from the string

# Join the set of unique characters into a single string
result_string = ''.join(unique_chars)

# Print the result
print(result_string)
list=[1,3,4,5,6,6]
print(set(list))
