def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict[1]

def sort_char_dictionary(chars):
    list = []
    for char in chars:
        list.append((char, chars[char]))
    list.sort()
    return list
