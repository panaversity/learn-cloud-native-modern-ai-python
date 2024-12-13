def build_person(first_name: str, last_name: str)->dict:
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician: dict = build_person('jimi', 'hendrix')
print(musician)