s = "AABABBAABBBAB"


def change_word():
    s1 = s.replace("A", "W").replace("B", "A").replace("W", "B")
    return s1


print(change_word())