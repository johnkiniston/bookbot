from stats import get_word_count,get_letter_count
import sys
def get_book_text(path):
    with open(path) as f:
        file_contents= f.read()
    return(file_contents)

def sort_text(text):
    list_of_dicts = []
    for ch, cnt in text.items():
        list_of_dicts.append({"char": ch, "num": cnt})

    def get_num(entry):
        return entry["num"]

    list_of_dicts.sort(key=get_num, reverse=True)

    return list_of_dicts

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text=get_book_text(sys.argv[1])
    num_words=get_word_count(book_text)
    leader=f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------"
    footer=f"============= END ==============="
    print (leader)
    print(f"Found {num_words} total words")
    
    #print(get_letter_count(book_text))
    #print(sort_text(get_letter_count(book_text)))

    print("--------- Character Count -------")

    sorted_counts = sort_text(get_letter_count(book_text))

    for entry in sorted_counts:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")
    print (footer)
    
main()
