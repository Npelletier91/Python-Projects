from collections import Counter

def find_non_repeated(string):
    char_count = Counter(string)
    for char in string:
        if char_count[char] == 1:
            print(char)


print(find_non_repeated("Hello World!"))
