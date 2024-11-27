def main():
    try:
        with open("/home/donp/boot.dev/workspace/github.com/dpnorth/bookbot/books/frankenstein.txt") as f:
            file_contents = f.read()
            print(file_contents)
    except Exception as e:
        print(f"Encountered exception {e}")


main()
