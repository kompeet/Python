def get_middle(s):
    if len(s) % 2:
        return s[int(len(s)/2)]
    else:
        return s[int((len(s)/2)-1)] + s[int(len(s)/2)]

s = "l"
print(get_middle(s))