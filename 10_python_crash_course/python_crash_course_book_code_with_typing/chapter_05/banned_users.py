banned_users:list[SyntaxWarning] = ['andrew', 'carolina', 'david']
user:str = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")