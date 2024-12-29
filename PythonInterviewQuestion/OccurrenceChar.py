# input_string = "ABCDABBCDABBBCCCDDEEEF"
# freq_chars={}
# for char in input_string:
#     if char not in freq_chars:
#         freq_chars[char]=1
#     else:
#         freq_chars[char]=freq_chars[char]+1
# print(freq_chars)

from collections import Counter

# Input string
input_string = "ABCDABBCDABBBCCCDDEEEF"

# Count the frequency of each character using Counter
freq_chars = Counter(input_string)

# Print the result
print(freq_chars)  # Output: Counter({'B': 7, 'C': 6, 'D': 4, 'A': 3, 'E': 3, 'F': 1})
