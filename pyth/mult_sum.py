def main():
  num1 = int(input("number1 = "))
  num2 = int(input("number2 = "))
  x = sum_mult(num1, num2)
  print(x)

def sum_mult(x, y):
  z = x * y
  if z < 1000:
    return z
  else:
    return x + y
  
main()