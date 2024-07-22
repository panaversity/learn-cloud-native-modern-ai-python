def get_formatted_name(first_name : str, middle_name: str, last_name: str)->str:
    """Return a full name, neatly formatted."""
    full_name: str = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician : str = get_formatted_name('john', 'lee', 'hooker')
print(musician)