import string

# print(string.ascii_letters)
# print(string.punctuation)
# print(string.hexdigits)
# print(string.digits)

test_str1 = 'The shells she sells are sea-shell5'
test_str2 = 'IntergallacticPython'
test_str3 = '419209'

res = "".join([c for c in test_str1 if c in string.ascii_letters])

# print(all([c.isalpha() for c in test_str1]))

# print(test_str1.isnumeric())
# print(test_str3.isnumeric())

# print(res)

# print(test_str1.isalnum())
# print(test_str2.isalpha())

sample_str = 'Peter Piper picked a peck of pickled peppers'

# print(sample_str.startswith('Peter'))
# print(sample_str.startswith('peter'))
# print(sample_str.endswith('peppers'))

# print(sample_str.find('picked'))
# print(sample_str.rfind('picked'))

new_str = sample_str.replace('pepper', 'apple')
# print(new_str)

# print(sample_str.count('a'))

sample_str2 = 'Betty Botter bought a bit of butter'

# print(sample_str2.upper())
# print(sample_str2.lower())

# split_res = sample_str2.split(" ")
# print(split_res)

# join_res = " ".join(split_res)
# print(join_res)

names = ["Doc", "Grumpy", "Bashful", "Sleepy", "Happy", "Sneezy", "Dopey"]
longest = max(len(name) for name in names)

# for name in names:
#     print(name.ljust(longest+2, "-") + ":")
# for name in names:
#     print(name.center(longest+2, "-") + ":")
# for name in names:
#     print(name.rjust(longest+2, "-") + ":")

the_str = "The quick brown $animal $action over the lazy dog"
the_template = string.Template(the_str)
# from string import Template
# output_str = the_template.substitute(animal='fox', action='jumped')
# print(output_str)

# args = {
#     "animal": "cow",
#     "action": "ran"
# }

# output_str = the_template.substitute(args)
# print(output_str)

product = "laptop"
price = "199.99"
tax = 0.08

print(f"{product} has a price of {price}, plus {tax:.2%} tax")