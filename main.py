from stats import *
path_to_file = "books/frankenstein.txt"
test_char_list = [{"char":"a","count":"100"},{"char":"b","count":"200"},{"char":"c","count":"300"},{"char":"d","count":"400"},{"char":",","count":"100"}]

def main():
    text = getBookText(path_to_file)
    word_count = getWordCount(text)
    char_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)
    print_report(path_to_file, word_count, chars_sorted_list)

def getBookText(path_to_file):
     with open(path_to_file) as f:
                return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
    
main()