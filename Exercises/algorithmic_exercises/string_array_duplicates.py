def no_dup(lst):
    non_dup = []
    for words in lst:
        for letters in words:
            while letters*2 in words:
                words = words.replace(letters*2,  letters)
        non_dup.append(words)
    return non_dup

test1 = ["LLLOOLL", "HHAABBIIBBII", "YYOOLLOO"]
print(no_dup(test1))









