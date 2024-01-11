def pangram(string):
    alphabet = set("qwertyuiopasdfghjklzxcvbnm")
    return set(string.lower()) >= alphabet

#setting the string makes each letter unique when checking if >=

print(pangram("hello wolrd!"))
print(pangram("qwer poiuty ajlshd lkjfg  mnb zxc v "))