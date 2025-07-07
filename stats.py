def count_words(text):
  words = text.split()
  return len(words)

def sort_by(items):
  return items["amount"]

def count_characters(text):
  count = {}
  for char in text.lower():
    if char in count:
      count[char] += 1
    else:
      count[char] = 1
  return count

def sort_characters(unsorted_dict):
  result = [{"char": char, "amount": amount} for char, amount in unsorted_dict.items()]
  result.sort(key=sort_by, reverse=True)
  return result
