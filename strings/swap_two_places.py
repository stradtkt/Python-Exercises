def swap_two_places(str1, str2):
  new_str_a = str2[:2] + str1[2:]
  new_str_b = str1[:2] + str2[2:]
  return new_str_a + ' ' + new_str_b

print(swap_two_places('abc', 'xyz'))