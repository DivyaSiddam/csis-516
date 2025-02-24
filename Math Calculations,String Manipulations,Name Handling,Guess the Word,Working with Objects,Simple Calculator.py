import math
import random

# Math Calculations
print("Math Calculations:")
print("Square root of 144:", math.sqrt(144))
print("Exponential value of 2 (e^2):", math.exp(2))
print("Sine and Cosine values of π/4 radians:")
print("Sine(π/4):", math.sin(math.pi / 4))
print("Cosine(π/4):", math.cos(math.pi / 4))
print("Remainder of 123 divided by 17 using fmod:", math.fmod(123, 17))

# Ask the user to input the radius of a circle and calculate the area and circumference
radius = float(input("\nEnter the radius of a circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")

# String Manipulations
print("\nString Manipulations:")
sentence = input("Enter a sentence: ")
print("Lowercase sentence:", sentence.lower())
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)
print("Number of vowels in the sentence:", vowel_count)
print("Reversed sentence:", sentence[::-1])

# Name Handling
print("\nName Handling:")
full_name = input("Enter your full name: ")
first_name, last_name = full_name.split()  # Assuming the name has two parts
print("First name:", first_name)
print("Last name:", last_name)
email = f"{first_name.lower()}.{last_name.lower()}@CSIS516.com"
print("Generated email:", email)

# Guess the Word
print("\nGuess the Word:")
word = input("Enter a word: ")
shuffled_word = ''.join(random.sample(word, len(word)))
print("Shuffled word:", shuffled_word)

# Working with Objects
print("\nWorking with Objects:")
char = input("Enter a character: ")
print(f"ASCII value of '{char}':", ord(char))
ascii_value = int(input("Enter an ASCII value: "))
print(f"Character for ASCII value {ascii_value}:", chr(ascii_value))

# Simple Calculator
print("\nSimple Calculator:")
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "Error: Division by zero is not allowed!"
    else:
        result = num1 / num2
else:
    result = "Invalid operator!"

print("Result:", result)
