def smallest_number(number_list):
  minimum = number_list[0]
  for i in number_list:
    if i < minimum:
      minimum = i
  return minimum

print(smallest_number([1,2,3,4,-1,-2,3,4,5]))