from stats import get_num_words, get_num_chars, report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1]
    book_text=get_book_text(path)
    num_words=get_num_words(book_text)
    char_counts=get_num_chars(book_text)
    report(num_words, char_counts,path)
    # print(f"{num_words} words found in the document")
    # print(char_counts)
if __name__=="__main__":
    main()