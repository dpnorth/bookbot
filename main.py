#!/usr/bin/python3
def main():
    file_path_and_name = "books/frankenstein.txt"
    file_contents = read_file(file_path_and_name)
    wc = word_count(file_contents)
    char_count_dict = character_count(file_contents)
    sorted_cc_dict = sort_dict(char_count_dict)
    #sorted_cc_dict = sort_dict_list(char_count_dict)

    print(f"--- Begin report of {file_path_and_name} ---")
    print(f"{wc} words found in the document\n")
    #for char in char_count_dict:
        #print(f"The '{char}' character was found {char_count_dict[char]} times")
    for char in sorted_cc_dict:
        if (char.isalpha()):
            print(f"The '{char}' character was found {sorted_cc_dict[char]} times")
    print("--- End report ---")


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


def read_file(file_name):
    base_path = "/home/donp/boot.dev/workspace/github.com/dpnorth/bookbot/"
    full_path = base_path + file_name
    try:
        with open(full_path) as f:
            file_contents = f.read()
    except Exception as e:
        print(f"Encountered exception {e}")
    return file_contents


def sort_dict(dict_in):
    sorted_dict = {}
    for key in sorted(dict_in, key=dict_in.get, reverse=True):
        sorted_dict[key] = dict_in[key]
    return sorted_dict


def sort_dict_list(dict_in):
    sorted_dict = {}
    dict_list = []
    for key in dict_in:
        dict_list.append({"key": key, "value" : dict_in[key]})
    dict_list.sort(reverse=True, key=sort_on)
    for i in range(0, len(dict_list)):
        key = dict_list[i]["key"]
        value = dict_list[i]["value"]
        sorted_dict[key] = value
    return sorted_dict


def sort_on(dict):
    return dict["value"]


def word_count(text):
    words = text.split()
    return len(words)


main()
