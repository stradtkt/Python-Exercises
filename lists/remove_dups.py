my_list = [10,10,20,20,20,10,23,23,90,90,34,56]

dups = set()
unique_items = []
for item in my_list:
  if item not in dups:
    unique_items.append(item)
    dups.add(item)

print(dups)