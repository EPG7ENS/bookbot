import sys
from stats import total_words, num_appears, sort_text_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()
        return file

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    filepath = sys.argv[1]
    file = get_book_text(filepath)
    num_appeared = num_appears(file)
    sorted_dicts = sort_text_chars(num_appeared)
    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}
----------- Word Count ----------
Found {total_words(file)} total words
--------- Character Count -------""")
    for section in sorted_dicts:
        if(section["char"].isalpha() == True):
            print(f"{section['char']}: {section['num']}")
        else:
            continue
    print("============= END ===============")
main()

