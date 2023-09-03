def main():
  """
  This function gets the user to enter an integer and prints it out.
  """

  x = get_int("What's x? ")
  print(f"x is {x}")


def get_int(x):
  """
  This function gets an integer from the user and returns it.
  """
  while True:
    try:
      return int(input(x))
    except ValueError:
      pass


main()