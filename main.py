print("---------------Bookbot Report---------------")


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in this book!")
    
    get_char_count(text)
    
    print("---------------Report End---------------")
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    char_count={}
    for char in text.lower():
        if char.isalpha():        
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char]=1
    print("Character Count:")
    for char in sorted(char_count):    
        print(f"The'{char}' was found {char_count[char]} times")


main()
