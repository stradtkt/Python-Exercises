sample_string = 'google.com'
sample_string_2 = "Hello, my name is Kevin Stradtman, and I am a developer"

def char_amount(str1):
  char_dict = {}
  for char in str1:
    keys = char_dict.keys()
    if char in keys:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict

print(char_amount(sample_string))
print(char_amount(sample_string_2))