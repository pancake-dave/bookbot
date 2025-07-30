def count_words(text):
    words_list = text.split()
    return f"{len(words_list)} words found in the document"

def count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict