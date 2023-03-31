def super_reduced_string(s):
    for letter in s:
        if letter*2 in s:
            s = s.replace(letter*2, "")
    if len(s) > 0:
        return s
    else:
        return "Empty String"



s = "aaaabbcsc"
print(super_reduced_string(s))