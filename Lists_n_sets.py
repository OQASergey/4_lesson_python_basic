print("** СПИСКИ **")
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

a = [1,2,3,4,[5,6,7]]
print(a[-1][0:2])

print("** МНОЖЕСТВА **")
# Множества (sets)

list01 = [1, 2, 3, 3, 3, 4, 4, 5]
print(list01)
set01 = set(list01)
set02 = {5, 5, 3, 7, 9, 12, 12}
list01_1 = list(set01)
print(list01_1)

set_un = set01.union(set02)
print(set_un)

print(set01.intersection(set02))
print(set01.difference(set02))

a = {1,2,2,3,3,3,4,5}
b = {2,4,12}
print(a.difference(b))

