def main():
  get = input("Input anything: ")
  print("Original String is", get)
  print("Printing only even index chars")
  for x in get[0::2]:
    print(x)
  
main()