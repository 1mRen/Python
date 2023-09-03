def main():
  x = 0
  print("Printing current and previous number sum in a range(10)")
  x = loop(x)
  print(x)
    
    
    
def loop(x):
  z = 0
  while x < 11:
    print(f"Current Number {x} Previous Number {z} Sum: {z + x}")
    while z < x:
      z += 1
    x += 1
    
main()