def get_char_map(book) -> dict[str, int]:
    book = str(book)
    book = book.lower()
    book_dict = {}

    for a in book:
        if a in book_dict:
            book_dict[a] = book_dict[a] + 1
        else:
            book_dict[a] = 1

    return book_dict


def print_report(num, dict_obj):
    print("--- Being report of books/frankenstein.txt ---")
    print(f"{num} words found the document\n\n")

    for x in dict_obj:
        if x[0].isalpha():
            print(f"The '{x[0]}' character was found {x[1]} times")


def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()

    words = file_contents.split()
    total_words = len(words)
    # print(total_words)

    char_count = get_char_map(file_contents)
    new_dict = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    # print(char_count["p"])

    print_report(total_words, new_dict)


if __name__ == "__main__":
    main()
