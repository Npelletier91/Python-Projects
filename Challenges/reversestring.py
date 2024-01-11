def reversestring(sentence):
    sentence = sentence.split()
    reversed_sentence = " ".join(reversed(sentence))
    return reversed_sentence

print(reversestring("hello world!"))