try:
    birth_year = int(input("What year were you born? "))
    age = 2025 - birth_year
    print(f"This year you will be {age} years old.")
except ValueError:
    print("Please enter a valid year.")