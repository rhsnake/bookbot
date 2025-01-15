path_to_file = "books/frankenstein.txt"

def main():
    text = getBookText(path_to_file)
    word_count = getWordCount(text)
    
    char_dict = get_char_dict(text)
    print(char_dict)


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
        

main()