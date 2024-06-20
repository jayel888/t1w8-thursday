def convert_to_integer(value):
    try:
        result = int(value)
        print(f"Conversional Successful! Result is {result}")
    except ValueError:
        print('Conversion failed. Please enter a valid integer.')
    finally:
        print("Closing any open resources")

# User input
user_input = input("Enter a number to convert to integer: ")

# Convert the number
convert_to_integer(user_input)