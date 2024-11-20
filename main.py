def main():
    filepath = "books/frankenstein.txt"
    text = get_text(filepath)
    number_of_words = count_words(text)
    number_of_char = count_characters(text)
    print(text)
    print(number_of_words)
    print(number_of_char)
    
    
def count_characters(string):
    appearances = {}
    lower = string.lower()
    for char in lower:
        if(char not in appearances):
            appearances[char] = 1
        else:
            appearances[char] += 1
    return appearances
    
def count_words(string):
    words = string.split()
    
    return len(words)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        
    return file_contents


main()