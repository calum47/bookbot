import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def main():
    # Require exactly one argument: the path to the book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            book_text = f.read()
    except OSError as e:
        print(f"Error: could not read file '{file_path}': {e}")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")
    char_counts = get_char_counts(book_text)
    for item in sort_char_counts(char_counts):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
