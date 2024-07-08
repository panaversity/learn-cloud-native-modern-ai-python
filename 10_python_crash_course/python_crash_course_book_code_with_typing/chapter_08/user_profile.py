def build_profile(first:str, last: str, **user_info:str)->dict:
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile:dict = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)