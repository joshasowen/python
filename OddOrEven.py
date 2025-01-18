number = int(input("Please Enter Your Number "))  # Input and convert it to an integer

if int(number / 2) * 2 == number:  # Check if the number divided by 2 and then multiplied by 2 equals the original number
    print(f"{number} is an even number.")  # If true, it's even
else:
    print(f"{number} is an odd number.")  # Otherwise, it's odd

