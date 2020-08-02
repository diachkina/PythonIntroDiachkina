print("* * * * *  * *  \t*     *\t\t*\t * *")
print("    *     *   * \t* *   *\t\t*\t*   *\n"
      "    *     * * * \t*  *  *\t\t*\t* * *\n"
      "    *     *   * \t*   * *\t\t*\t*   *\n"
      "    *     *   * \t*     *\t\t*\t*   *")


text = input()
text = text.split()
quantity_words = {}
for key_word in text:
    quantity_words[key_word] = text.count(key_word)
    # quantity_words[key_word] = quantity_words.get(key_word, 0) + 1
print(quantity_words)

max_value = max(list(quantity_words.values()))
word = ''
for key, value in quantity_words.items():
    if value == max_value:
        word = key


print(word, max_value)
