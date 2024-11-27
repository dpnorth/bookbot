def main():
    file_path_and_name = "books/frankenstein.txt"
    file_contents = read_file(file_path_and_name)
    wc = word_count(file_contents)
    char_count_dict = character_count(file_contents)
    print(f"--- Begin report of {file_path_and_name} ---")
    print(f"{wc} words found in the document\n")
    for char in char_count_dict:
        print(f"The '{char}' character was found {char_count_dict[char]} times")
    print("--- End report ---")


def read_file(file_name):
    base_path = "/home/donp/boot.dev/workspace/github.com/dpnorth/bookbot/"
    full_path = base_path + file_name
    try:
        with open(full_path) as f:
            file_contents = f.read()
    except Exception as e:
        print(f"Encountered exception {e}")
    return file_contents


def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    low_text = text.lower()
    char_cnt_dict = {}
    for i in range(0, len(low_text)):
        char = low_text[i]
        if (char in char_cnt_dict):
            char_cnt_dict[char] += 1
        else:
            char_cnt_dict[char] = 1
    return char_cnt_dict


main()
