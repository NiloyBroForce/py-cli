import sys

from stats import word_count,char_count,chars_dict_to_sorted_list 
def get_book_text(path)->str:
    with open(path) as f:
      file_contents = f.read()
    return file_contents

def print_report(path,wordcount,charlist):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for l in charlist:
        if l[0].isalpha():
            print(f"{l[0]}: {l[1]}")
    print("============= END ===============")

def main():
    if(len(sys.argv))!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1]

    bookstr=get_book_text(path)
    char_dict=char_count(bookstr)
    my_list=chars_dict_to_sorted_list(char_dict)

    print_report(path,word_count(bookstr),my_list)
  
main()
