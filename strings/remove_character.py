def remove_character(str, i):
  first = str[:i]
  last = str[i+1:]
  return first + last
string = "Hello my name is Kevin"
print(remove_character(string, 1))
print(remove_character(string, 2))
print(remove_character(string, 6))