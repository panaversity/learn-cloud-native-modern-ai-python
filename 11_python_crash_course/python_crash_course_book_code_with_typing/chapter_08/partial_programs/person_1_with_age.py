from typing import Optional, Union

def build_person(first_name: str, last_name: str, age: Union[int,None] = None) -> dict:
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age is not None:
        person['age'] = age
    return person

musician: dict = build_person('jimi', 'hendrix', age=27)
print(musician)
