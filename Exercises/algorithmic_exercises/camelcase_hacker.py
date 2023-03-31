import re

def camel_case(text):
    text = re.split("[A-Z]", text)
    print(text)
    return len(text)

text = "lcameCaseLolLolLolLol"
print(camel_case(text))