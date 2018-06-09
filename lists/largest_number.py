def largest_number(number_list):
  maximum = number_list[0]
  for i in number_list:
    if i > maximum:
      maximum = i
  return maximum

print(largest_number([1,2,3,4,5,6,7,8,56,43]))