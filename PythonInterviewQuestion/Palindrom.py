pal = "aamaaq"
n = len(pal)
for x in range(n // 2):
    if pal[x] != pal[n - x - 1]:
        print("Not palindrom number")
        break;
else:
    print("Palindrom number")

if pal == pal[::-1]:
    print("Palindrom number")
else:
    print("Not palindrom number")


def is_palindrome(input_string):
    return input_string == input_string[::-1]


input_string = "madam"
if is_palindrome(input_string):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
