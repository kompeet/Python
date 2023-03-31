def ransom_note(magazine, note):
    word_dict = {}
    output = "YES"
    for i in magazine:
        word_dict[i] = word_dict.get(i,0) + 1
    for j in note:
        if word_dict.get(j,0) != 0:
            word_dict[j] -= 1
        else:
            output = "NO"
            break
    return output

