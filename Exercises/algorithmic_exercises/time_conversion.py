def time_conversion(s):
    hour = "12"
    if s[-2:] == "PM":
        if s[:2] != "12":
            hour = str(int(s[:2]) + int(12))
    else:
        if s[:2] == "12":
            hour = "00"
        else:
            hour = s[:2]
    return hour + s[2:-2]

s = "07:05:45PM"
print(time_conversion(s))