def count_vowels(string) -> int:
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


string = "hellO worldE"
vowel_count = count_vowels(string)
print(vowel_count)
