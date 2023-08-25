import re

### *

# print(re.search('ave-*coder', 'avecoder'))

# print(re.search('ave-*coder', 'ave-coder'))

# print(re.search('ave-*coder', 'ave--coder'))

### +

# print(re.search('ave-+coder', 'avecoder'))

# print(re.search('ave-+coder', 'ave-coder'))

# print(re.search('ave-+coder', 'ave--coder'))

### ?

# print(re.search('ave-?coder', 'avecoder'))

# print(re.search('ave-?coder', 'ave-coder'))

# print(re.search('ave-?coder', 'ave--coder'))

### *? +? ??

# print(re.search('<.*>', '%<ave> <coder> <coderz>%'))

# print(re.search('<.*?>', '%<ave> <coder> <coderz>%'))

# print(re.search('<.+>', '%<ave> <coder> <coderz>%'))

# print(re.search('<.+?>', '%<ave> <coder> <coderz>%'))

# print(re.search('av?', 'ave'))

# print(re.search('av??', 'aveeeee'))

### {m}

print(re.search('x-{3}x', 'x--x'))

print(re.search('x-{3}x', 'x---x'))

print(re.search('x-{3}x', 'x----x'))

### {m,n}

# for i in range(1, 10):
#     s = f"x{'-' * i}x"
#     print(f'{i}  {s:10}', re.search('x-{2,5}x', s))
