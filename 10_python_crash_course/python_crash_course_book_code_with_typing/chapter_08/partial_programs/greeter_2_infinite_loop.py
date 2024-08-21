def get_formatted_name(first_name: str, last_name: str)->str:
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name: str = input("First name: ")
    l_name: str = input("Last name: ")

    formatted_name: str = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")