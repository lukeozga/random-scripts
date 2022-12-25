# Generate all combinations of strings with specified maximum
# lenght and set of characters to use

def gen_strings(length, charset):
    charset = [*charset]
    strings = charset

    for i in range(1, length):
        temp = []
        for k in range(len(strings)):
            string = strings[k]
            if i == 1:
                temp.append(string)
            for m in range(len(charset)):
                letter = charset[m]
                temp.append(string + letter)
        strings = temp
    return(strings)