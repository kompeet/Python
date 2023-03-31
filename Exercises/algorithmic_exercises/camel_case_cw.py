def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    words = text.split()
    return "".join([i.capitalize() if i != words[0] else i for i in words])

test1 = "the_stealth_warrior"
print(to_camel_case(test1))
