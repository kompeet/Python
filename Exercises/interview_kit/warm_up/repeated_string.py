def repeatedString(s, n):
    if len(s) ==1:
        if s[0]=='a':
            return n
    count = 0
    for i in s:
        if i == 'a':
            count+=1
    sus = n//len(s)
    count *= sus
    for i in s[:n-(sus*len(s))]:
        if i == 'a':
            count+=1
    return count