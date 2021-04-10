def count_letter(words, letter):
  count = 0
  for word in words:
    if letter in word:
      count += 1
  return count

words = ['python', 'c++', 'c', 'scala', 'java']
letter = 'c'

print(count_letter(words, letter))