def disem_vowel(string):
    split_list = list(string)
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    result = []

    for letter in split_list:
        if letter not in vowels:
            result.append(letter)
    return "".join(result)

string = "aaaaa"
print(disem_vowel(string))



