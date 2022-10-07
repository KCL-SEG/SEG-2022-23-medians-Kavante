"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

length = int(len(numbers))
median = 0.0
numbers = sorted(numbers)

if length % 2 == 0:
    median = (numbers[(length//2)-1] + numbers[length//2] ) / 2
else:
    median = numbers[ ((length+1)//2)-1]
print(median)
