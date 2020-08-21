file = open('text.txt', 'w', encoding='utf-8')
while True:
    text = input()
    if text == "":
        break
    file.write(text + "\n")
file.close()
