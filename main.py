def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    character_counts = count_characters(file_contents)
    sorted_chars = get_sorted_list(character_counts)


    print(f"{word_count} words found in the document\n")
    
    for char_dict in sorted_chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    total_characters = {}
    
    for character in text:
        lowered_character = character.lower()
        if lowered_character in total_characters:
            total_characters[lowered_character] += 1
        else:
            total_characters[lowered_character] = 1     
    
    return total_characters

def sort_on(dict):
    return dict["count"]

def get_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()