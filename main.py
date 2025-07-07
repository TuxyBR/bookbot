def get_book_text(filepath):
  with open(filepath) as f:
    content = f.read()
  return content

def count_words(text):
  words = text.split()
  return len(words)

def main():
  path = "books/frankenstein.txt"
  book = get_book_text(path)
  count = count_words(book)
  print(f"{count} words found in the document")

main()