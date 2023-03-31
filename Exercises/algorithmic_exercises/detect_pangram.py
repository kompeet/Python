def is_pangram(s):
    lst = []
    s = s.lower()
    for i in s:
        if i.isalpha():
            if i not in lst:
                lst.append(i)
    return len(lst) == 26


s = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(s))