def find_longest_word(word_list):
  words = []
  for word in word_list:
    words.append((len(word), word))
  words.sort()
  return words[-1][1]

print(find_longest_word(["Hello", "my", "name", "Jessica"]))