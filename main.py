path_to_file = "books/frankenstein.txt"
test_char_list = [{"char":"a","count":"100"},{"char":"b","count":"200"},{"char":"c","count":"300"},{"char":"d","count":"400"},{"char":",","count":"100"}]

def main():
    text = getBookText(path_to_file)
    word_count = getWordCount(text)
    
    char_dict = get_char_dict(text)
    sorted_char_list = sort_char_dict(char_dict)
    
    book_report(word_count,sorted_char_list)


def getBookText(path_to_file):
     with open(path_to_file) as f:
                return f.read()

def getWordCount(text):
    count = len(text.split())
    return count


def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def sort_char_dict(char_dict):
    sorted_list =[]
    for ch in char_dict:
        sorted_list.append({"char": ch, "count": char_dict[ch]})
    sorted_list.sort(reverse= True, key= sort_on)
    return sorted_list
    
    
def book_report(word_count,char_list):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    for c in char_list:
        if not c["char"].isalpha():
            continue
        print(f"The '{c["char"]}' character was found {c["count"]} times.")

    print("--- End report ---")
    
main()