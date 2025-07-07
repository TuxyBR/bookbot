def get_book_text(filepath):
  with open(filepath) as f:
    content = f.read()
  return content

def main():
  path = "books/frankenstein.txt"
  print(get_book_text(path))

main()