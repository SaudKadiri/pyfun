def morse(word):
  morse = lambda i: [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.","---", ".--.",
                     "--.-", ".-.", "...", "-","..-", "...-", ".--", "-..-","-.--","--.."][i]
  index = lambda letter: ord(letter) - ord('a')
  word_to_morse = lambda word: ''.join(map(morse, map(index, word)))
  return word_to_morse(word.lower())

# Playground
print(morse('saud'))  # ....-..--..
print(morse('blest')) # -....-......-
