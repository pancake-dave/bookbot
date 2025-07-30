from stats import count_words, count_characters

def get_new_text(file_path):
    with open(file_path) as f:
        text = f.read()
        return text

def main():
    print(count_words(get_new_text("books/frankenstein.txt")))
    print(count_characters(get_new_text("books/frankenstein.txt")))

main()