def long_prefix(text):
    letters = zip(*text)
    result = ""

    for char in letters:
        if len(set(char)) > 1:
            break
        result += char[0]
    return result

text = ["thor", "thomas", "thiago"]
print(long_prefix(text))















