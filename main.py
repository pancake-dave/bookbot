from stats import count_words, count_characters, character_count_lists

def get_new_text(file_path):
    with open(file_path) as f:
        text = f.read()
        return text

def main():
    path = "books/frankenstein.txt"
    text = get_new_text(path)
    word_count = count_words(text)
    char_count = count_characters(text)
    char_dicts_list = character_count_lists(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in char_dicts_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()