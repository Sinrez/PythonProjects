import re

#### []

# print(re.search('co[dn]e','avecoder'))

# print(re.search('co[dn]e','cones'))

# print(re.search('[a-z]','avecoder'))
# print(re.search('[A-Z]','aVecoder'))




### ^

# print(re.search('[0-9]','000avecoder'))
# print(re.search('[^0-9]','000avecoder'))
# print(re.search('[0-9^]','000avecoder'))

### - 

# print(re.search('[-ave]', '000-ave'))
# print(re.search('[ave-]', '000-ave'))
# print(re.search('[a\-ve]', '000-ave'))

### ]

# print(re.search('[]]', 'ave :]'))
# print(re.search('[\]]', 'ave :]'))

### (.)

# print(re.search('av.coder', 'avecoder'))
# print(re.search('ave.coder', 'avecoder'))

### \w  == [a-zA-Z0-9_]

# print(re.search('\w', 'avecoder'))
# print(re.search('\w', '.v-#?/]|['))

### \W = [^a-zA-Z0-9_]

# print(re.search('\W', '.v-#?/]|['))
# print(re.search('\W', 'a*ecoder'))

### \d

# print(re.search('\d', 'av3coder'))

### \D

print(re.search('\D', 'av3coder'))

### \s

# print(re.search('\s', 'ave coder'))

### \S

# print(re.search('\S', '      |      '))

#########

# print(re.search('[\d\w\s]', '-------0-------'))

#########

### \

# print(re.search('.', 'avecoder.com'))
# print(re.search('\.', 'avecoder.com'))

# rs = r'directory\folder'

# print(re.search(r'\\', rs))
# print(re.search('\\\\', rs))