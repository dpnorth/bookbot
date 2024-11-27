def main():
    try:
        with open("/home/donp/boot.dev/workspace/github.com/dpnorth/bookbot/books/frankenstein.txt") as f:
            file_contents = f.read()
            #print(file_contents)
            #wc = word_count(file_contents)
            #print(f"word count {wc}")
            print(character_count(file_contents))
    except Exception as e:
        print(f"Encountered exception {e}")

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
