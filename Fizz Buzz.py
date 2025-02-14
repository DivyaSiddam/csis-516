for number in range(1, 101):
  # First check if the number is divisible by both 3 and 5.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
 
  # Then check if the number is only divisible by 3
  elif number % 3 == 0:
    print("Fizz")
 
  # Finally check if the number is only divisible by 5
  elif number % 5 == 0:
    print("Buzz")
 
  # If it's not divisible by either of those numbers, just print the number
  else:
    print(number)
