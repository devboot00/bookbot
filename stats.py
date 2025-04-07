def get_num_words(text):
    words=text.split()
    return len(words)

def get_num_chars(text):
    text=text.lower()
    char_counts={}
    for c in text:
        char_counts[c]=char_counts.get(c,0)+1
    return char_counts

def report(num_words, char_counts,path):
    sorted_counts=sorted(char_counts.items(),key=lambda x:x[1],reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing the book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c,count in sorted_counts:
        if c.isalpha():
            print(f"{c}: {count}")
    print("============= END ===============")
