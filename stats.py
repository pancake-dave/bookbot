def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def character_count_lists(dict):
    def sort_on(items):
        return items["num"]

    car_dicts_list = []
    for char, number in dict.items():
        car_dicts_list.append({"char": char, "num": number})
    car_dicts_list.sort(reverse=True, key=sort_on)

    return car_dicts_list