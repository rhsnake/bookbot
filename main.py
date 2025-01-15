path_to_file = "books/frankenstein.txt"

def main():
    text = getBookText(path_to_file)
    word_count = getWordCount(text)
    print(f"{word_count} words found in book.")
    

def getBookText(path_to_file):
     with open(path_to_file) as f:
                return f.read()

def getWordCount(text):
    count = len(text.split())
    return count
    
main()