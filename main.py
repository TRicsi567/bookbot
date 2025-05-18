import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    num_words = get_num_words(content) 
    char_counts = get_char_counts(content)
    sorted_char_counts = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_counts:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
        

    print("============= END ===============")

main()
