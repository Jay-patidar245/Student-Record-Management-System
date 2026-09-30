def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_mark(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_choice(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Please enter a valid integer.")
