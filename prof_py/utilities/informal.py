def get_name(person):
    fname = person.get('fname','')
    lname = person.get('lname','')
    name = f"{fname} {lname}"
    return name