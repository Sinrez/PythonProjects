def get_name(person):
    title = person.get('title','')
    fname = person.get('fname','')
    lname = person.get('lname','')
    if title:
        name = f"{title} {fname} {lname}"
    else:
        name = f"{fname} {lname}"
    return name