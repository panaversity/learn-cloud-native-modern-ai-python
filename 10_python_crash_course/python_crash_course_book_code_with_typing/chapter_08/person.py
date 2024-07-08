from typing import Optional

def build_person(first_name: str, last_name: str, age: Optional[int] = None) -> dict:
    """
    Return a dictionary of information about a person.

    :param first_name: The first name of the person.
    :param last_name: The last name of the person.
    :param age: The age of the person, which is optional.
    :return: A dictionary containing the person's information.
    """
    person = {'first': first_name, 'last': last_name}
    if age is not None:
        person['age'] = age  # No need for a type hint here
    return person

musician: dict = build_person('jimi', 'hendrix', age=27)
print(musician)
