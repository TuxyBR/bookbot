import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
  with open(filepath) as f:
    content = f.read()
  return content

def print_stats(path, count, characters):
  print("============ BOOKBOT ============")
  print(f"Analysis book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {count} total words")
  print("--------- Character Count -------")
  for char in characters:
    if char['char'].isalpha():
      print(f"{char['char']}: {char['amount']}")
  print("============= END ===============")

def main():
  if len(sys.argv) == 2:
    path = sys.argv[1]
  else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book = get_book_text(path)
  count = count_words(book)
  characters = count_characters(book)
  sorted = sort_characters(characters)
  print_stats(path, count, sorted)

main()