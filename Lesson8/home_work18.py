text = input()
text = text.split()
quantity_words = {}
for key_word in text:
    quantity_words[key_word] = text.count(key_word)
print(quantity_words)

max_value = max(list(quantity_words.values()))
word = ''
for key, value in quantity_words.items():
    if value == max_value:
        word = key


print(word, max_value)
