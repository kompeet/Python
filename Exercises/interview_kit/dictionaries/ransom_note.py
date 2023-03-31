def check_magazine(magazine, note):
    dict_note = {}
    output = 'Yes'
    for i in magazine:
        dict_note[i] = dict_note.get(i, 0) + 1
    for j in note:
        if dict_note.get(j, 0) != 0:
            dict_note[j] -= 1
        else:
            output = 'No'
            break
    print(output)

a = "give me one grand today night"
b = "give one grand today"
check_magazine(a,b)