text = input().split()
quantity_words = {}
for key_word in text:
    value_quantity = text.count(key_word)
    quantity_words[key_word] = value_quantity
print(quantity_words)