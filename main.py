def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print("\n")
    word_count(text)
    print("\n")
    final_dict = character_count(text)
    # Sorting the dictionary by values in descending order
    sorted_chars = sorted(final_dict.items(), key=lambda item: item[1], reverse=True)

# Iterating through the sorted list and printing the results
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    print(f"The book has {len(words)} words")


def character_count(text):
    my_string = text
    lowered_string = my_string.lower()
    filtered_string = ''.join(char for char in lowered_string if char.isalpha())
    text_dict = {}
    
    for my_char in filtered_string:
        if my_char in text_dict:
            text_dict[my_char] += 1
        else:
            text_dict[my_char] = 1

    return text_dict

    
          







main()