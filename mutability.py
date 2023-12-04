# 1. Списки, словани и множества изменяемы
# 2. Кортежи и frozenset - нет

# 1

a = [1,2,3]
aa = a
print(a)
print(aa)

aa.append(4)
print(a)
print(aa)

print("==============")
#=======
b = [1,2,3]
bb = b.copy()
print(b)
print(bb)
b.append(4)
print(b)
print(bb)

print("==============")
#=======
a = [1,2,3,[4,5]]
b = a.copy()
print(a)
print(b)

b.append(7)
print(a)
print(b)

b[-2].append(6)
print(a)
print(b)

print("==============")
#=======
from copy import deepcopy
a = [1,2,[3,4]]
b = deepcopy(a)
print(a)
print(b)

b[-1].append(5)
print(b)
print(a)







