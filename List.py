lst = ['Mango', 'Blueberry', 'Strawberry', 'Raspberry', 'Passion fruit']

print("length of list:", len(lst))
print("first element:", lst[0])
print("last element:", lst[-1])

lst.append ("Raspberry")
print("updated list", lst)

lst.remove ("Passion fruit")
print("updated list", lst)

lst.sort()
print("updated list", lst)

lst.pop(1)
print("updated list", lst)

lst.reverse()
print("updated list", lst)

print("multiplication on list", lst*2)

lst=lst[:4]
print("sliced list", lst)

lst.clear()
print("updated list", lst)
