def main():
    filepath = "books/frankenstein.txt"
    text = get_text(filepath)
    number_of_words = count_words(text)
    number_of_char = count_characters(text)
    char_count = to_list(number_of_char)
    print(f"--- Begin report of {filepath}")
    print(f"{number_of_words} found in the document\n")

    for obj in char_count:
        ch, num = obj
        print(f"The '{ch}' character was found {num} times")
    print("--- End report ---")


def to_list(dic):
    lis = []
    for key in dic:
        lis.append((key, dic[key]))
    lis.sort(reverse = True, key = lambda x:x[1])
    return lis
 
def count_characters(string):
    appearances = {}
    lower = string.lower()
    for char in lower:
        if(char.isalpha()):
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