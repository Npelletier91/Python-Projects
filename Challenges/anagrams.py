def anagram(string1,string2):
    sorted_string1 = sorted(string1.lower())
    sorted_string2 = sorted(string2.lower())
    return sorted_string1 == sorted_string2

#   or only
#   return sorted(string1) == sorted(string2)


print(anagram("listen", "Silent"))
print(anagram("listen", "Silence"))