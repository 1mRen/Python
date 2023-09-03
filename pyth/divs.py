def main():
  given = [10, 20, 33, 46, 55]
  print("Divisible by 5")
  
  for x in given:
    if x % 5 == 0:
      print(x)
    else:
      continue
main()