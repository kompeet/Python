def pig_it(text):
    text = text.split()
    lst = []
    for word in text:
        if word.isalpha():
            lst.append(word[1:] + word[0] + "ay")
        else:
            lst.append(word)
    return " ".join(lst)


    # text = text.split()
    # return ' '.join( [word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text])

text = "LOL lol noob N00B!"
print(pig_it(text))
