import re

def match_item(text):
  patterns = '^[a-z]+_[a-z]+$'
  if re.search(patterns, text):
    return 'Found a match'
  else:
    return "No match here"

print(match_item("aaa_bbb"))
print(match_item("-----__-----"))
print(match_item("Ab_Cd_Ef"))