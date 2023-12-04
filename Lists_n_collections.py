# список (list)

list1 = [1, 2, 3, "a", "b", "c"]
list2 = [1, 2, "a", ["b", 3]]
list3 = [5, 2, 4, 1, 3]
list4 = ["a", "c", "d", "b"]

print(list1[0])
print(list1[:4])
print(list2[-1])

s_list3 = sorted(list3)
print(s_list3)
print(list3)

print(list4)
list4.sort()
print(list4) #list4 уже отредактирован безвозвратно