def onlyvowels(string):
    vowels = "aeiou"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count
    
print(onlyvowels("hello world!"))
