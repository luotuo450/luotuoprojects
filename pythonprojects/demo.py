list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = list(map(sum, zip(list1, list2)))
print(result)
