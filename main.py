path_to_file = "books/frankenstein.txt"

def main():
    text = getBookText(path_to_file)
    print(text)
    

def getBookText(path_to_file):
     with open(path_to_file) as f:
                return f.read()


main()