import re

### ^ ### \A ###

print(re.search('^ave', 'avecoder'))
print(re.search('^ave', 'coderave'))

print(re.search('\Aave', 'avecoder'))
print(re.search('\Aave', 'coderave'))

### $ ### \Z ###

# print(re.search('coder$', 'avecoder'))
# print(re.search('coder$', 'coderave'))

# print(re.search('coder\Z', 'avecoder'))
# print(re.search('coder\Z', 'coderave'))

# print(re.search('coder$', 'avecoder\n'))

### \b ###

# print(re.search(r'\bcoder', 'ave coder'))
# print(re.search(r'\bcoder', 'ave.coder'))
# print(re.search(r'\bcoder', 'avecoder'))

# print(re.search(r'coder\b', 'ave coder'))
# print(re.search(r'coder\b', 'ave.coder'))
# print(re.search(r'coder\b', 'avecoder'))

# print(re.search(r'\bcoder\b', 'ave coder moder'))
# print(re.search(r'\bcoder\b', 'ave(coder)moder'))
# print(re.search(r'\bcoder\b', 'avecodermoder'))

### \B ###

# print(re.search(r'\Bcoder\B', 'coder'))
# print(re.search(r'\Bcoder\B', '.coder.'))
# print(re.search(r'\Bcoder\B', 'ave coder moder'))
# print(re.search(r'\Bcoder\B', 'avecodermoder'))























