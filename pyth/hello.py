def main():
  #ask user for their name
  username = input("Please enter your name: ").title()
  hello(username)


def hello(to="world!"):
  print("Hello,", to)
  

main()