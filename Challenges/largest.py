def largestele(list):
    for item in list:
        largest = item
        if item > largest:
            item = largest
    return largest

list = [1,4,23,53,3,6,39]
print(largestele(list))
