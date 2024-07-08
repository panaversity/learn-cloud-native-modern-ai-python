def greet_users(names:list[str])->None:
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames :list[str] = ['hannah', 'ty', 'margot']
greet_users(usernames)