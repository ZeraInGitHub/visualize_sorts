def string_to_list(string: str) -> list:
    k = 0
    result = []
    for _ in range(string.count(',') + 1):
        seperated = ''
        while string[k] == ',' or string[k] == ' ':
            k += 1
        for i in range(len(string)):
            if k >= len(string):
                break
            if string[k] == ',':
                break
            seperated += string[k]
            k += 1
        result.append(seperated)
    return result

if __name__ == '__main__':
    print(string_to_list('hello, hi, world'))