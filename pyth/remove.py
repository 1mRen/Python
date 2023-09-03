def main():
  char = input("Input a word: ")
  n = int(input("Number of words you wish to remove: "))
  x = remove_char(char, n)
  print(x)
  
def remove_char(char, n):
  print('\nOriginal string:', char)
  x = char[n:]
  return x
  
main()