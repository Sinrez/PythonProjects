from utilities import names
from utilities import informal
from utilities import casual
from utilities import account

community = [{
    "title": "Mr.",
    "fname": "John",
    "lname": "Smith"
} for x in range(3)]

# print(community)
for person in community:
    tone = account.get_tone()
    if tone == "formal":
        get_name = names.get_name(person)
    elif tone == "informal":
        get_name = informal.get_name(person)
    elif tone == "casual":
        get_name = casual.get_name(person)
    else:
        get_name = names.get_name(person)
    print(get_name)