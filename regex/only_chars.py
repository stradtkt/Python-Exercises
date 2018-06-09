import re 

def only_chars(string):
  charRe = re.compile(r'[^a-zA-Z0-9.]')
  string = charRe.search(string)
  return not bool(string)

print(only_chars('abcdefg123456787'))
# true
print(only_chars("&^%$#@abcd"))
# false