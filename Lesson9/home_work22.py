def season(c):
    if 2 < c < 6:
        return "spring"
    elif 5 < c < 9:
        return "summer"
    elif 8 < c < 12:
        return "autumn"
    else:
        return "winter"

print(season(4))
