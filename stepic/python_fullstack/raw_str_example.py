not_raw_str = 'Not\tRaw\nString'

#print(not_raw_str)

raw_str = r'Not\tRaw\nString'

print(raw_str)

print(type(not_raw_str))
print(type(raw_str))

print(r'Not\tRaw\nString' == 'Not\\tRaw\\nString')

print(len(not_raw_str))
print(len(raw_str))

print(list(not_raw_str))
print(list(raw_str))

########

path = 'C:\\Windows\\system32\\cmd.exe'
rpath = r'C:\Windows\system32\cmd.exe'

print(path == rpath)

path2 = 'C:\\Windows\\system32\\'
rpath2 = r'C:\Windows\system32' + '\\'

print(path2 == rpath2)

#########################

s_r = repr(not_raw_str)
print(s_r)

print(list(s_r))

s_r2 = repr(not_raw_str)[1:-1]
print(s_r2)

print(raw_str == s_r2)

print(r'\t' == repr('\t')[1:-1])